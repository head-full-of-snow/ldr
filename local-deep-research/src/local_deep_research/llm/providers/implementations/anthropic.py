"""Anthropic LLM provider for Local Deep Research."""

from langchain_anthropic import ChatAnthropic
from loguru import logger

from ....config.thread_settings import (
    get_setting_from_snapshot,
    NoSettingsContextError,
)
from ..openai_base import OpenAICompatibleProvider


class AnthropicProvider(OpenAICompatibleProvider):
    """Anthropic provider for Local Deep Research.

    This is the official Anthropic API provider.
    """

    provider_name = "Anthropic"
    api_key_setting = "llm.anthropic.api_key"
    default_model = "u2"  # User must explicitly pick a model — no silent fallback
    default_base_url = "https://maas-api.hivoice.cn/anthropic"
    # https://maas-api.hivoice.cn/anthropic
    # https://api.anthropic.com/v1

    # Metadata for auto-discovery
    provider_key = "ANTHROPIC"
    company_name = "Anthropic"
    is_cloud = True

    @classmethod
    def create_llm(cls, model_name=None, temperature=0.7, **kwargs):
        """Factory function for Anthropic LLMs.

        Args:
            model_name: Name of the model to use
            temperature: Model temperature (0.0-1.0)
            **kwargs: Additional arguments including settings_snapshot

        Returns:
            A configured ChatAnthropic instance

        Raises:
            ValueError: If API key is not configured
        """
        settings_snapshot = kwargs.get("settings_snapshot")

        # Get API key from settings
        api_key = get_setting_from_snapshot(
            cls.api_key_setting,
            default=None,
            settings_snapshot=settings_snapshot,
        )

        # Check for custom base URL (self-hosted endpoints may not require API key)
        custom_url = get_setting_from_snapshot(
            "llm.anthropic.base_url",
            default=None,
            settings_snapshot=settings_snapshot,
        )
        has_custom_url = custom_url and str(custom_url).strip()

        if not api_key:
            if has_custom_url:
                api_key = "dummy-key-for-custom-endpoint"
            else:
                logger.error(
                    f"{cls.provider_name} API key not found in settings")
                raise ValueError(
                    f"{cls.provider_name} API key not configured. "
                    f"Please set {cls.api_key_setting} in settings."
                )

        # Require an explicit model — no silent fallback to a hardcoded default.
        if not model_name or not model_name.strip():
            logger.error(f"{cls.provider_name} model name not provided")
            raise ValueError(
                f"{cls.provider_name} model not configured. "
                f"Please set llm.model in settings "
                f"(e.g. 'claude-3-5-sonnet-20241022')."
            )

        # Build Anthropic-specific parameters
        anthropic_params = {
            "model": model_name,
            "anthropic_api_key": api_key,
            "temperature": temperature,
        }

        # Support custom base URL for self-hosted Anthropic-compatible endpoints
        if has_custom_url:
            anthropic_params["anthropic_api_url"] = str(custom_url).strip()

        # Add max_tokens if specified in settings
        try:
            max_tokens = get_setting_from_snapshot(
                "llm.max_tokens",
                default=None,
                settings_snapshot=settings_snapshot,
            )
            if max_tokens:
                anthropic_params["max_tokens"] = int(max_tokens)
        except NoSettingsContextError:
            pass  # Optional parameter

        logger.info(
            f"Creating {cls.provider_name} LLM with model: {model_name}, "
            f"temperature: {temperature}"
        )

        return ChatAnthropic(**anthropic_params)

    @classmethod
    def is_available(cls, settings_snapshot=None):
        """Check if this provider is available.

        Args:
            settings_snapshot: Optional settings snapshot to use

        Returns:
            True if API key is configured or custom base URL is set, False otherwise
        """
        try:
            # Check if API key is configured
            api_key = get_setting_from_snapshot(
                cls.api_key_setting,
                default=None,
                settings_snapshot=settings_snapshot,
            )
            if api_key and str(api_key).strip():
                return True

            # Also available if a custom base URL is set (self-hosted endpoint)
            custom_url = get_setting_from_snapshot(
                "llm.anthropic.base_url",
                default=None,
                settings_snapshot=settings_snapshot,
            )
            return bool(custom_url and str(custom_url).strip())
        except Exception:
            return False
