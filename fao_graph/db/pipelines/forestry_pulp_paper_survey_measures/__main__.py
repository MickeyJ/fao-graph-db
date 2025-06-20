"""Run forestry_pulp_paper_survey_measures migration"""
from .forestry_pulp_paper_survey_measures import ForestryPulpPaperSurveyMeasuresMigrator
from fao_graph.logger import logger


def run_migration():
    """Execute forestry_pulp_paper_survey_measures migration"""
    try:
        migrator = ForestryPulpPaperSurveyMeasuresMigrator()
        migrator.migrate()
        migrator.verify_migration()
    except Exception as e:
        logger.error(f"Migration failed: {e}")
        raise


if __name__ == "__main__":
    run_migration()