from os import environ
from typing import Any, cast

import pytest
from BL_Python.programming.config import AbstractConfig
from BL_Python.programming.str import get_random_str
from BL_Python.web.application import (
    configure_blueprint_routes,
    configure_openapi,
    create_app,
)
from BL_Python.web.config import Config, FlaskConfig
from flask_injector import FlaskInjector
from mock import MagicMock
from pydantic import BaseModel
from pytest_mock import MockerFixture

from ..create_app import CreateApp, FlaskClientConfigurable


class TestCreateApp(CreateApp):
    # TODO extend blueprint and openapi tests to cover each relevant config attribute
    def test__configure_blueprint_routes__creates_flask_app_using_config(
        self, mocker: MockerFixture
    ):
        flask_mock = mocker.patch("BL_Python.web.application.Flask")

        app_name = f"{TestCreateApp.test__configure_blueprint_routes__creates_flask_app_using_config.__name__}-app_name"

        with pytest.raises(
            RuntimeError, match=r"^app is not a valid flask.app.Flask app instance$"
        ):
            _ = configure_blueprint_routes(Config(flask=FlaskConfig(app_name=app_name)))

        flask_mock.assert_called_with(app_name)

    def test__configure_blueprint_routes__requires_flask_config(self):
        with pytest.raises(
            Exception,
            match=r"^Flask configuration is empty\. Review the `flask` section of your application's `config\.toml`\.$",
        ):
            _ = configure_blueprint_routes(Config())

    @pytest.mark.parametrize("filename", ["foo", "foo.py", "__main__.py"])
    def test__configure_blueprint_routes__when_discovering_blueprints_ignores_directories_in_path(
        self, filename: str, mocker: MockerFixture
    ):
        mocker.stop(
            self._automatic_mocks["BL_Python.web.application._import_blueprint_modules"]
        )

        _ = mocker.patch("BL_Python.web.application._get_program_dir", return_value=".")
        _ = mocker.patch("BL_Python.web.application._get_exec_dir", return_value=".")

        spec_lookup_mock = mocker.patch("importlib.util.spec_from_file_location")
        glob_item_mock = MagicMock(
            is_file=MagicMock(
                # fakes a directory
                return_value=False
            )
        )
        type(glob_item_mock).name = filename
        with mocker.patch(
            "pathlib.Path",
            return_value=MagicMock(
                glob=MagicMock(
                    return_value=[
                        MagicMock(
                            is_file=MagicMock(
                                # fakes a directory
                                return_value=False
                            ),
                            # fakes a non-Python filename
                            name=filename,
                        )
                    ]
                ),
            ),
        ):
            app_name = f"{TestCreateApp.test__configure_blueprint_routes__when_discovering_blueprints_ignores_directories_in_path.__name__}-app_name"

            flask_app = configure_blueprint_routes(
                Config(
                    flask=FlaskConfig(app_name=app_name),
                ),
                ".",
            )

        assert not spec_lookup_mock.called
        assert flask_app.blueprints == {}

    @pytest.mark.parametrize(
        "is_file,filename",
        [
            (True, "foo"),
            (True, "foo.py"),
            (True, "__main__.py"),
            (True, "__init__.py"),
            (False, "__init__.py"),
        ],
    )
    def test__configure_blueprint_routes__when_discovering_blueprints_registers_python_files_and_modules(
        self, is_file: bool, filename: str, mocker: MockerFixture
    ):
        mocker.stop(
            self._automatic_mocks["BL_Python.web.application._import_blueprint_modules"]
        )

        _ = mocker.patch("BL_Python.web.application._get_program_dir", return_value=".")
        _ = mocker.patch("BL_Python.web.application._get_exec_dir", return_value=".")

        glob_item_mock = MagicMock(
            is_file=MagicMock(
                # fakes a directory
                return_value=is_file
            )
        )
        type(glob_item_mock).name = filename
        with mocker.patch(
            "pathlib.Path",
            return_value=MagicMock(
                glob=MagicMock(return_value=[glob_item_mock]),
            ),
        ):
            spec_lookup_mock = mocker.patch("importlib.util.spec_from_file_location")
            _ = mocker.patch("importlib.util.module_from_spec")

            app_name = f"{TestCreateApp.test__configure_blueprint_routes__when_discovering_blueprints_ignores_directories_in_path.__name__}-app_name"

            flask_app = configure_blueprint_routes(
                Config(
                    flask=FlaskConfig(app_name=app_name),
                ),
                ".",
            )

        spec_lookup_mock.assert_called()
        assert flask_app.blueprints == {}

    def test__configure_blueprint_routes__when_discovering_blueprints_stops_when_module_load_fails(
        self, mocker: MockerFixture
    ):
        mocker.stop(
            self._automatic_mocks["BL_Python.web.application._import_blueprint_modules"]
        )

        _ = mocker.patch("BL_Python.web.application._get_program_dir", return_value=".")
        _ = mocker.patch("BL_Python.web.application._get_exec_dir", return_value=".")

        glob_item_mock = MagicMock(
            is_file=MagicMock(
                # fakes a directory
                return_value=True
            )
        )
        type(glob_item_mock).name = "__init__.py"
        _ = mocker.patch("importlib.util.spec_from_file_location", return_value=None)
        _ = mocker.patch("importlib.util.module_from_spec")
        with mocker.patch(
            "pathlib.Path",
            return_value=MagicMock(
                glob=MagicMock(return_value=[glob_item_mock]),
            ),
        ):
            app_name = f"{TestCreateApp.test__configure_blueprint_routes__when_discovering_blueprints_ignores_directories_in_path.__name__}-app_name"

            with pytest.raises(
                Exception,
                match=rf"^Module cannot be created from path {glob_item_mock}$",
            ):
                _ = configure_blueprint_routes(
                    Config(
                        flask=FlaskConfig(app_name=app_name),
                    ),
                    ".",
                )

    def test__configure_openapi__requires_flask_config(self):
        with pytest.raises(
            Exception,
            match=r"^OpenAPI configuration is empty\. Review the `openapi` section of your application's `config\.toml`\.$",
        ):
            _ = configure_openapi(Config())

    def test__create_app__requires_flask_config(
        self, flask_client_configurable: FlaskClientConfigurable
    ):
        with pytest.raises(
            Exception,
            match=r"^You must set \[flask\] in the application configuration\.$",
        ):
            _ = flask_client_configurable(Config())

    def test__create_app__loads_config_from_toml(
        self, basic_config: Config, mocker: MockerFixture
    ):
        load_config_mock = mocker.patch(
            "BL_Python.web.application.load_config", return_value=basic_config
        )

        toml_filename = f"{TestCreateApp.test__create_app__loads_config_from_toml.__name__}-config.toml"
        _ = create_app(config_filename=toml_filename)
        assert load_config_mock.called
        assert load_config_mock.call_args and load_config_mock.call_args[0]
        assert load_config_mock.call_args[0][1] == toml_filename

    def test__create_app__uses_custom_config_types(self, mocker: MockerFixture):
        toml_filename = f"{TestCreateApp.test__create_app__uses_custom_config_types.__name__}-config.toml"
        toml_load_result = {
            "flask": {
                "app_name": f"{TestCreateApp.test__create_app__uses_custom_config_types.__name__}-app_name"
            },
            "custom": {"foo": get_random_str(k=26)},
        }

        _ = mocker.patch("toml.load", return_value=toml_load_result)

        class CustomConfig(BaseModel, AbstractConfig):
            foo: str = get_random_str(k=26)

        app = create_app(
            config_filename=toml_filename, application_configs=[CustomConfig]
        )
        assert (
            cast(FlaskInjector, cast(Any, app).injector).injector.get(CustomConfig).foo
        ) == toml_load_result["custom"]["foo"]

    @pytest.mark.parametrize(
        "envvar_name,config_var_name,var_value",
        [
            ("FLASK_APP", "app_name", "foobar"),
            ("FLASK_ENV", "env", "barfoo"),
        ],
    )
    def test__create_app__updates_flask_config_from_envvars(
        self,
        envvar_name: str,
        config_var_name: str,
        var_value: str,
        basic_config: Config,
        mocker: MockerFixture,
    ):
        object.__setattr__(basic_config.flask, config_var_name, var_value)

        environ.update({envvar_name: var_value})
        _ = mocker.patch(
            "BL_Python.web.application.load_config", return_value=basic_config
        )
        _ = create_app()

        assert object.__getattribute__(basic_config.flask, config_var_name) == var_value

    @pytest.mark.parametrize(
        "envvar_name,config_var_name,var_value,should_fail",
        [
            ("FLASK_APP", None, "foobar", False),
            ("FLASK_ENV", None, "barfoo", False),
            (None, "app_name", "foobar", False),
            (None, "app_name", "", True),
            (None, "env", "barfoo", False),
        ],
    )
    def test__create_app__requires_application_name(
        self,
        envvar_name: str | None,
        config_var_name: str | None,
        var_value: str,
        should_fail: bool,
        mocker: MockerFixture,
    ):
        environ.update({"FLASK_APP": "", "FLASK_ENV": ""})

        if envvar_name is not None:
            environ.update({envvar_name: var_value})

        toml_load_result = {}
        if config_var_name is not None:
            toml_load_result["flask"] = {config_var_name: var_value}

        _ = mocker.patch("toml.load", return_value=toml_load_result)

        if should_fail:
            with pytest.raises(Exception):
                _ = create_app()
        else:
            _ = create_app()
