from policy_gradients_jax.ppo import main, Config


if __name__ == "__main__":
    Config.num_envs = 1
    main(None)