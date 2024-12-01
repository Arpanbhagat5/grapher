# Define the name of the virtual environment
VENV = grapher

# Default target (runs when you type `make`)
default: setup

# Target to set up the virtual environment
setup:
	@if [ ! -d "$(VENV)" ]; then \
		echo "Creating virtual environment: $(VENV)"; \
		python3 -m venv $(VENV); \
	else \
		echo "Virtual environment $(VENV) already exists."; \
	fi
	@echo "Activating virtual environment and installing dependencies..."
	@source $(VENV)/bin/activate && pip install --upgrade pip && pip install -r requirements.txt
	@echo "Setup complete. To activate the environment, run:"
	@echo "source $(VENV)/bin/activate"

# Target to run the script
run:
	@source $(VENV)/bin/activate && python grapher.py

# Target to clean up the environment
clean:
	@echo "Removing virtual environment..."
	@rm -rf $(VENV)
	@echo "Environment cleaned."
