import yaml
import pytest

from cobra.semantico.mod_validator import validar_mod


def _write_yaml(path, data):
    path.write_text(yaml.safe_dump(data))


def test_validador_archivo_faltante(tmp_path):
    mod = tmp_path / "m.co"
    data = {str(mod): {"version": "0.1.0", "python": str(tmp_path / "m.py")}}
    _write_yaml(tmp_path / "cobra.mod", data)
    with pytest.raises(ValueError):
        validar_mod(str(tmp_path / "cobra.mod"))


def test_validador_campos_faltantes(tmp_path):
    """Debe fallar si falta la clave python y js en una entrada."""
    mod = tmp_path / "x.co"
    data = {str(mod): {"version": "0.1.0"}}
    _write_yaml(tmp_path / "cobra.mod", data)
    with pytest.raises(ValueError):
        validar_mod(str(tmp_path / "cobra.mod"))


def test_validador_version_incorrecta(tmp_path):
    py = tmp_path / "m.py"
    py.write_text("x = 1")
    mod = tmp_path / "m.co"
    data = {str(mod): {"version": "bad", "python": str(py)}}
    _write_yaml(tmp_path / "cobra.mod", data)
    with pytest.raises(
        ValueError,
        match="^Archivo cobra.mod inválido: ",
    ):
        validar_mod(str(tmp_path / "cobra.mod"))


def test_validador_duplicados(tmp_path):
    py = tmp_path / "dup.py"
    py.write_text("x = 1")
    data = {
        str(tmp_path / "a.co"): {"version": "0.1.0", "python": str(py)},
        str(tmp_path / "b.co"): {"version": "0.1.0", "python": str(py)},
    }
    _write_yaml(tmp_path / "cobra.mod", data)
    with pytest.raises(ValueError):
        validar_mod(str(tmp_path / "cobra.mod"))
