import sys
from utils.logger import logger

from .datasets.production_crops_livestock import production_crops_livestock
from .datasets.production_indices import production_indices
from .datasets.trade_detailed_trade_matrix import trade_detailed_trade_matrix
from .datasets.trade_crops_livestock import trade_crops_livestock
from .datasets.trade_crops_livestock_indicators import trade_crops_livestock_indicators
from .datasets.trade_indices import trade_indices

datasets = [
    production_crops_livestock,
    production_indices,
    trade_detailed_trade_matrix,
    trade_crops_livestock,
    trade_crops_livestock_indicators,
    trade_indices,
]

if __name__ == "__main__":
    # Example usage
    # check sys arguments to use a specific dataset

    if len(sys.argv) > 1:
        dataset_name = sys.argv[1]
        query_name = sys.argv[2]

        if dataset_name in [dataset.__name__ for dataset in datasets]:
            for dataset in datasets:
                if dataset.__name__ == dataset_name:
                    explorer = dataset()
                    if query_name:
                        explorer.execute(query_name)
                    else:
                        explorer.execute()
                    break
        else:
            logger.error(f"Dataset '{dataset_name}' not found. Available datasets: {[d.__name__ for d in datasets]}")
    else:
        logger.error("Usage: python -m src.explore.datasets <dataset_name> <optional:query_name>")
