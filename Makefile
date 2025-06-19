include .env
export

# =-=-=--=-=-=-=-=-=-=
#   Environment Setup
# =-=-=--=-=-=-=-=-=-=

# Check for environment and set activation command
ifdef VIRTUAL_ENV
    # Already in a virtual environment
    ACTIVATE = @echo "venv - $(VIRTUAL_ENV)" &&
    PYTHON = python
else ifdef CONDA_DEFAULT_ENV
    # Already in conda environment  
    ACTIVATE = @echo "conda - $(CONDA_DEFAULT_ENV)" &&
    PYTHON = python
else ifeq ($(wildcard venv/Scripts/activate),venv/Scripts/activate)
    # Windows venv available
    ACTIVATE = @venv\Scripts\activate &&
    PYTHON = python
else ifeq ($(wildcard venv/bin/activate),venv/bin/activate)
    # Unix venv available
    ACTIVATE = @source venv/bin/activate &&
    PYTHON = python3
else
    # No environment found
    ACTIVATE = @echo "❌ No environment found. Run 'make venv' or activate conda." && exit 1 &&
    PYTHON = python
endif

.PHONY: venv env-status install-init install install-update install-requirements \
		db-use-remote db-use-local db-use-local-admin \
		db-test-connection-local neo4j-create-schema-local neo4j-reset-local \
		neo4j-migrate-reference-data-local neo4j-migrate-production-crops-livestock-local \
		neo4j-migrate-inputs-fertilizers-nutrient-local \
		INTERNAL-neo4j-migrate-production-crops-livestock INTERNAL-neo4j-reset \
		INTERNAL-neo4j-migrate-reference-data INTERNAL-db-test-connection \
		INTERNAL-neo4j-create-schema db-explore db-visual-phase1-all db-visual-phase1 \
		db-size-info-local create-db-local drop-db-local-admin clear-all-tables-local \
		db-size show-all-tables NO-DIRECT-USE-create-db NO-DIRECT-USE-drop-db \
		NO-DIRECT-USE-reset-db NO-DIRECT-USE-clear-all-tables \



# =-=-=--=-=-=-=-=-=-=
#  Python Environment
# =-=-=--=-=-=-=-=-=-=
venv:
	@$(PYTHON) -m venv venv
	@echo "✅ Virtual environment created. Activate with:"
	@echo "   source venv/bin/activate  (macOS/Linux)"
	@echo "   venv\\Scripts\\activate     (Windows)"

env-status:
	@echo "=== Environment Status ==="
	$(ACTIVATE) echo "Python: $$(which $(PYTHON))"

# =-=-=--=-=-=-=-=-=-=
# Package Installation
# =-=-=--=-=-=-=-=-=-=
install-init:
	$(ACTIVATE) $(PYTHON) -m pip install pip-tools
	$(ACTIVATE) $(PYTHON) -m piptools compile requirements.in
	$(ACTIVATE) $(PYTHON) -m piptools sync requirements.txt

install:
	grep "^${pkg}" requirements.in || echo "${pkg}" >> requirements.in
	$(ACTIVATE) $(PYTHON) -m piptools compile requirements.in
	$(ACTIVATE) $(PYTHON) -m piptools sync requirements.txt

install-update:
	$(ACTIVATE) $(PYTHON) -m piptools compile requirements.in
	$(ACTIVATE) $(PYTHON) -m piptools sync requirements.txt

install-requirements:
	$(ACTIVATE) $(PYTHON) -m piptools sync requirements.txt

# =-=-=--=-=-=-=-=-
#   ENV commands
# =-=-=--=-=-=-=-=-

db-use-remote:
	cp remote.env .env
	@echo "Switched to remote database"

db-use-local:
	cp local.env .env
	@echo "Switched to local database"

db-use-local-admin:
	cp local-admin.env .env
	@echo "Switched to local database as admin"


# =-=-=--=-=-=-=-=-=-=-=--=-=-=-=-=-
# 				Database/Neo4j 
# =-=-=--=-=-=-=-=-=-=-=--=-=-=-=-=-

db-test-connection-local:
	$(MAKE) db-use-local
	$(MAKE) INTERNAL-db-test-connection

neo4j-create-schema-local:
	$(MAKE) db-use-local
	$(MAKE) INTERNAL-neo4j-create-schema

neo4j-reset-local:
	$(MAKE) db-use-local
	$(MAKE) INTERNAL-neo4j-reset

neo4j-migrate-reference-data-local:
	$(MAKE) db-use-local
	$(MAKE) INTERNAL-neo4j-migrate-reference-data

neo4j-migrate-production-crops-livestock-local:
	$(MAKE) db-use-local
	$(MAKE) INTERNAL-neo4j-migrate-production-crops-livestock

neo4j-migrate-inputs-fertilizers-nutrient-local:
	$(MAKE) db-use-local
	$(MAKE) INTERNAL-neo4j-migrate-inputs-fertilizers-nutrient

neo4j-migrate-prices-local:
	$(MAKE) db-use-local
	$(MAKE) INTERNAL-neo4j-migrate-prices

INTERNAL-neo4j-migrate-prices:
	$(ACTIVATE) $(PYTHON) -m src.neo4j.migrate_prices $(ARGS)

INTERNAL-neo4j-migrate-inputs-fertilizers-nutrient:
	$(ACTIVATE) $(PYTHON) -m src.neo4j.migrate_inputs_fertilizers_nutrient $(ARGS)

INTERNAL-neo4j-migrate-production-crops-livestock:
	$(ACTIVATE) $(PYTHON) -m src.neo4j.migrate_production_crops_livestock $(ARGS)

INTERNAL-neo4j-reset:
	$(ACTIVATE) $(PYTHON) -m src.neo4j.schema reset

INTERNAL-neo4j-migrate-reference-data:
	$(ACTIVATE) $(PYTHON) -m src.neo4j.migrate_reference_data

INTERNAL-db-test-connection:
	$(ACTIVATE) $(PYTHON) -m src.core.test_connection

INTERNAL-neo4j-create-schema:
	$(ACTIVATE) $(PYTHON) -m src.neo4j.schema

# =-=-=--=-=-=-=-=-=-=-=--=-=-=-=-=-
# 			Database Exploration
# =-=-=--=-=-=-=-=-=-=-=--=-=-=-=-=-

db-explore:
	$(ACTIVATE) $(PYTHON) -m src.explore $(filter-out $@,$(MAKECMDGOALS))

db-visual-phase1-all:
	@echo "Running all Phase 1 visualizations..."
	@mkdir -p visuals/phase1
	@for sql in sql/explore/phase1/*.sql; do \
		echo "Processing $$sql..."; \
		python -m utils.create_table_visual "$$sql" -o visuals/phase1; \
	done

db-visual-phase1:
	$(MAKE) db-use-local
	$(ACTIVATE) $(PYTHON) -m utils.create_table_visual sql/explore/phase1/$(sql_file).sql


# =-=-=--=-=-=-=-=-=-=-=--=-=-=-=-=-
# 			Database Mod and Info
# =-=-=--=-=-=-=-=-=-=-=--=-=-=-=-=-

db-size-info-local:
	$(MAKE) db-use-local-admin
	$(MAKE) db-size
	$(MAKE) db-use-local

create-db-local:
	$(MAKE) db-use-local-admin
	@echo " "
	@echo "Creating local database 'fao'..."
	$(MAKE) NO-DIRECT-USE-create-db
	$(MAKE) db-use-local

drop-db-local-admin:
	$(MAKE) db-use-local-admin
	@echo " "
	@echo "Dropping local database 'fao_analysis'..."
	@echo " "
	$(MAKE) NO-DIRECT-USE-drop-db name=fao_analysis
	@echo " "
	@echo "Database 'fao_analysis' dropped"
	@echo " "
	$(MAKE) db-use-local

clear-all-tables-local:
	$(MAKE) db-use-local
	@echo " "
	@echo "Clear all local tables..."
	$(MAKE) NO-DIRECT-USE-clear-all-tables
	$(MAKE) db-use-local

db-size:
	@echo "Showing all tables in the database..."
	psql "postgresql://$(DB_USER):$(DB_PASSWORD)@$(DB_HOST):$(DB_PORT)/$(DB_NAME)" -f sql/db_size_stats.sql

show-all-tables:
	@echo "Showing all tables in the database..."
	psql "postgresql://$(DB_USER):$(DB_PASSWORD)@$(DB_HOST):$(DB_PORT)/$(DB_NAME)" -f sql/select_all_tables.sql

NO-DIRECT-USE-create-db:
	psql "postgresql://$(DB_USER):$(DB_PASSWORD)@$(DB_HOST):$(DB_PORT)/postgres" -f sql/create_database.sql

NO-DIRECT-USE-drop-db:
	psql "postgresql://$(DB_USER):$(DB_PASSWORD)@$(DB_HOST):$(DB_PORT)/postgres" -c "DROP DATABASE IF EXISTS ${name};"

NO-DIRECT-USE-reset-db:
	@echo "Resetting database..."
	psql "postgresql://$(DB_USER):$(DB_PASSWORD)@$(DB_HOST):$(DB_PORT)/$(DB_NAME)" -f sql/drop_tables.sql

NO-DIRECT-USE-clear-all-tables:
	@echo "Showing all tables in the database..."
	psql "postgresql://$(DB_USER):$(DB_PASSWORD)@$(DB_HOST):$(DB_PORT)/$(DB_NAME)" -f sql/clear_all_tables.sql
