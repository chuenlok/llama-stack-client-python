# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from llama_stack_client import LlamaStackClient, AsyncLlamaStackClient
from llama_stack_client.types import HealthInfo

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestInspect:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_health(self, client: LlamaStackClient) -> None:
        inspect = client.inspect.health()
        assert_matches_type(HealthInfo, inspect, path=["response"])

    @parametrize
    def test_method_health_with_all_params(self, client: LlamaStackClient) -> None:
        inspect = client.inspect.health(
            x_llama_stack_provider_data="X-LlamaStack-ProviderData",
        )
        assert_matches_type(HealthInfo, inspect, path=["response"])

    @parametrize
    def test_raw_response_health(self, client: LlamaStackClient) -> None:
        response = client.inspect.with_raw_response.health()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        inspect = response.parse()
        assert_matches_type(HealthInfo, inspect, path=["response"])

    @parametrize
    def test_streaming_response_health(self, client: LlamaStackClient) -> None:
        with client.inspect.with_streaming_response.health() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            inspect = response.parse()
            assert_matches_type(HealthInfo, inspect, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncInspect:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_health(self, async_client: AsyncLlamaStackClient) -> None:
        inspect = await async_client.inspect.health()
        assert_matches_type(HealthInfo, inspect, path=["response"])

    @parametrize
    async def test_method_health_with_all_params(self, async_client: AsyncLlamaStackClient) -> None:
        inspect = await async_client.inspect.health(
            x_llama_stack_provider_data="X-LlamaStack-ProviderData",
        )
        assert_matches_type(HealthInfo, inspect, path=["response"])

    @parametrize
    async def test_raw_response_health(self, async_client: AsyncLlamaStackClient) -> None:
        response = await async_client.inspect.with_raw_response.health()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        inspect = await response.parse()
        assert_matches_type(HealthInfo, inspect, path=["response"])

    @parametrize
    async def test_streaming_response_health(self, async_client: AsyncLlamaStackClient) -> None:
        async with async_client.inspect.with_streaming_response.health() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            inspect = await response.parse()
            assert_matches_type(HealthInfo, inspect, path=["response"])

        assert cast(Any, response.is_closed) is True