import pytest
import subprocess
from pathlib import Path
import sys

# Ruta del binario externo
ANALYZER_PATH = "/usr/bin/external-analyzer"


def run_external_analyzer(args):
    """Invoca el binario externo usando subprocess.run"""
    return subprocess.run(
        [ANALYZER_PATH] + args,
        capture_output=True,
        text=True
    )


@pytest.fixture
def fake_analyzer_path():
    return str(Path(__file__).parent / "stubs" / "fake-analyzer.sh")


def test_analyzer_success(monkeypatch, fake_analyzer_path):
    # Redirige la variable global al stub
    monkeypatch.setattr(
        sys.modules[__name__],
        "ANALYZER_PATH",
        fake_analyzer_path
    )
    result = run_external_analyzer(["success"])
    assert result.returncode == 0
    assert "Análisis exitoso" in result.stdout


def test_analyzer_failure(monkeypatch, fake_analyzer_path):
    monkeypatch.setattr(
        sys.modules[__name__],
        "ANALYZER_PATH",
        fake_analyzer_path
    )
    result = run_external_analyzer(["failure"])
    assert result.returncode == 1
    assert "Error en el análisis" in result.stdout


def test_analyzer_timeout(monkeypatch, fake_analyzer_path):
    monkeypatch.setattr(
        sys.modules[__name__],
        "ANALYZER_PATH",
        fake_analyzer_path
    )
    result = run_external_analyzer(["timeout"])
    assert result.returncode == 124
    assert "Tiempo de espera agotado" in result.stdout
