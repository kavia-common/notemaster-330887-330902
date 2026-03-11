"""
Minimal FastAPI application for notes_backend.

This repository snapshot previously contained only environment/configuration files,
which prevented PreviewManager from starting the backend dependency. This module
provides a small but valid FastAPI app with a health endpoint.

The full notes CRUD/auth functionality can be layered on later; for preview
readiness we must expose a stable HTTP server and /healthz endpoint.
"""

from __future__ import annotations

from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI(
    title="Notes Backend API",
    description="Backend service for the Notes app (preview-ready minimal implementation).",
    version="0.1.0",
    openapi_tags=[
        {"name": "health", "description": "Service health and readiness endpoints."},
    ],
)


class HealthResponse(BaseModel):
    """Response model for health checks."""

    status: str = Field(..., description="Overall service status.")
    service: str = Field(..., description="Service identifier.")


@app.get(
    "/healthz",
    tags=["health"],
    summary="Health check",
    description="Used by PreviewManager/readiness probes to confirm the backend is running.",
    response_model=HealthResponse,
    operation_id="healthz",
)
def healthz() -> HealthResponse:
    # PUBLIC_INTERFACE
    """Return a simple health status for readiness checks."""
    return HealthResponse(status="ok", service="notes_backend")
