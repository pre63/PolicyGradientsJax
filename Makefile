install:
	@[ -d .venv ] || python3.11 -m venv .venv
	@. .venv/bin/activate && pip install -r requirements.txt

test:
	@. .venv/bin/activate && PYTHONPATH=. python policy_gradients_jax/ppo.py

fix:
	@. .venv/bin/activate && (black policy_gradients_jax && isort policy_gradients_jax)

clean:
	@rm -rf .venv
	@rm -rf ./**/__pycache__