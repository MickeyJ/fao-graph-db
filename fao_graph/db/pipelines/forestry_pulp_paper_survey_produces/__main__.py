"""Run forestry_pulp_paper_survey_produces migration"""
from .forestry_pulp_paper_survey_produces import ForestryPulpPaperSurveyProducesMigrator
from fao_graph.logger import logger


def run_migration():
    """Execute forestry_pulp_paper_survey_produces migration"""
    try:
        migrator = ForestryPulpPaperSurveyProducesMigrator()
        migrator.migrate()
        migrator.verify_migration()
    except Exception as e:
        logger.error(f"Migration failed: {e}")
        raise


if __name__ == "__main__":
    run_migration()