"""Run forestry_pulp_paper_survey_consumes migration"""
from .forestry_pulp_paper_survey_consumes import ForestryPulpPaperSurveyConsumesMigrator
from fao_graph.logger import logger


def run_migration():
    """Execute forestry_pulp_paper_survey_consumes migration"""
    try:
        migrator = ForestryPulpPaperSurveyConsumesMigrator()
        migrator.migrate()
        migrator.verify_migration()
    except Exception as e:
        logger.error(f"Migration failed: {e}")
        raise


if __name__ == "__main__":
    run_migration()