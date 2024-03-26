from dataclasses import dataclass

import hydra
from hydra.core.config_store import ConfigStore
from omegaconf import OmegaConf


@dataclass
class DataSetConfig:
    """To specify the structure of the data set configuration."""

    name: str
    path: str


@dataclass
class Config:
    """Main configuration class."""

    dataset: DataSetConfig


# hydra does not know that we want the config to be of type Config
# so we specify this using a config store where we link to the Config data class
cs = ConfigStore.instance()
cs.store(name="custom_config", node=Config)


# decorator to let hydra know that it needs to load the configuration before
# running the main function
@hydra.main(version_base=None, config_path="conf", config_name="config")
def process_config(cfg: Config) -> None:
    """Hierarchical configuration from multiple sources.
    A outputs folder is created for each run.

    Args:
        cfg (Config): Main config file.
    """
    print(cfg.dataset)
    print(OmegaConf.to_yaml(cfg))

    # check that the configuration is valid
    Config(**cfg)

    # check if the config is valid
    DataSetConfig(**cfg.dataset)


if __name__ == "__main__":
    process_config()
