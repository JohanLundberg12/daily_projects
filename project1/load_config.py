from dataclasses import dataclass

import hydra
from omegaconf import DictConfig, OmegaConf


@dataclass
class DataSetConfig:
    name: str
    path: str


@hydra.main(version_base=None, config_path="conf", config_name="config")
def process_config(cfg: DictConfig) -> None:
    """Hierarchical configuration from multiple sources.
    A outputs folder is created for each run.

    Args:
        cfg (DictConfig): Main config file.
    """
    print(OmegaConf.to_yaml(cfg))

    # check if the config is valid using dataclass
    DataSetConfig(**cfg.dataset)


if __name__ == "__main__":
    process_config()
