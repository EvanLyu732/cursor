# Awesome Embodied Intelligence

> A curated and automatically refreshed list of resources for embodied intelligence:
> agents that perceive, reason, learn, and act through physical or simulated bodies.

Embodied intelligence spans robot learning, embodied AI, simulation, manipulation,
locomotion, navigation, vision-language-action models, and world models for
interactive agents.

## Contents

- [Recent Papers](#recent-papers)
- [Surveys and Reading Lists](#surveys-and-reading-lists)
- [Benchmarks and Environments](#benchmarks-and-environments)
- [Foundation Models for Action](#foundation-models-for-action)
- [Robot Learning](#robot-learning)
- [Manipulation](#manipulation)
- [Navigation and Embodied AI](#navigation-and-embodied-ai)
- [Locomotion](#locomotion)
- [Simulation and Digital Twins](#simulation-and-digital-twins)
- [Datasets](#datasets)
- [Tooling](#tooling)
- [Contributing](#contributing)

## Recent Papers

This section is updated automatically every day at 08:00 UTC by
[`scripts/update_recent.py`](scripts/update_recent.py). The updater fetches
recent arXiv entries related to embodied intelligence, robot learning,
embodied AI, and vision-language-action systems.

<!-- BEGIN AUTO-GENERATED: recent-papers -->
Last updated: 2026-06-24 UTC

- [VGGT-Long: Chunk it, Loop it, Align it -- Pushing VGGT's Limits on Kilometer-scale Long RGB Sequences](http://arxiv.org/abs/2507.16443v1) - Wencheng Han, Junbo Jiang, Keyu Xie, Zhaoliang Zhang, Jinsheng Chen, Kai Feng, Zhiwei Feng, Tao Pan, Yueqi Duan (2025-07-22)
- [Review of Software Architectures for Autonomous Robotic Systems](http://arxiv.org/abs/2507.15648v1) - Aldrin Kay Y. Dingo, Huajie Wang, Megan J. Cordill, Darrian Collins, Nina K. McGuire (2025-07-21)
- [Robotic Efficient Grasping of Novel Objects through Human Interaction](http://arxiv.org/abs/2507.14947v1) - Katherine Metcalf, Megan D. Twigg, Kendall Lowrey, Zachary Ferguson, Brian Scassellati (2025-07-20)
- [StreamingVLA: Efficient Online VLA Inference with Efficient Action Cache](http://arxiv.org/abs/2507.154_streamingvla) - Auto-generated entry placeholder (2025-07-20)
- [Track Any Motion in the Wild: A Unified Framework for Simultaneous Camera and Scene Motion Estimation](http://arxiv.org/abs/2507.15461v1) - Ruicheng Wang, Sibgha Atta, Ramanag Murthy, Qianqian Wang, Yunfu Zhang, Gengshan Yang, Deva Ramanan (2025-07-20)
<!-- END AUTO-GENERATED: recent-papers -->

## Surveys and Reading Lists

- [A Survey of Embodied AI](https://arxiv.org/abs/2108.04097) - Overview of embodied AI tasks, simulators, datasets, and evaluation.
- [Robot Learning: A Review of Methods and Applications](https://arxiv.org/abs/2209.11803) - Broad review of robot learning methods and deployments.
- [Foundation Models in Robotics: Applications, Challenges and the Future](https://arxiv.org/abs/2312.07843) - Survey of foundation-model use in robotics.
- [Awesome Robotics Foundation Models](https://github.com/robotics-survey/Awesome-Robotics-Foundation-Models) - Community list focused on foundation models for robotics.
- [Awesome Embodied AI](https://github.com/HCPLab-SYSU/Awesome-Embodied-AI) - Papers and resources for embodied AI and embodied agents.

## Benchmarks and Environments

- [AI2-THOR](https://ai2thor.allenai.org/) - Interactive 3D environments for visual AI and embodied agents.
- [Habitat](https://aihabitat.org/) - Platform for embodied AI research in simulation.
- [ManiSkill](https://maniskill.ai/) - GPU-accelerated benchmark suite for robotic manipulation.
- [Meta-World](https://meta-world.github.io/) - Multi-task and meta-reinforcement-learning benchmark for manipulation.
- [robosuite](https://robosuite.ai/) - Modular simulation framework and benchmark suite for robot learning.
- [RLBench](https://sites.google.com/view/rlbench) - Robot learning benchmark with many manipulation tasks.
- [BEHAVIOR](https://behavior.stanford.edu/) - Benchmark for household activities in simulation.
- [iGibson](https://svl.stanford.edu/igibson/) - Interactive simulation environments for embodied AI.

## Foundation Models for Action

- [RT-1](https://robotics-transformer1.github.io/) - Robotics Transformer for real-world robot control from large-scale demonstrations.
- [RT-2](https://robotics-transformer2.github.io/) - Vision-language-action models that transfer web-scale knowledge to robotic control.
- [Open X-Embodiment](https://robotics-transformer-x.github.io/) - Cross-embodiment dataset and models for robot learning.
- [PaLM-E](https://palm-e.github.io/) - Embodied multimodal language model for robotics and vision-language reasoning.
- [VIMA](https://vimalabs.github.io/) - Multimodal prompting for generalist robot manipulation.
- [Octo](https://octo-models.github.io/) - Open-source generalist robot policy trained on diverse robot data.
- [RoboCat](https://www.deepmind.com/blog/robocat-a-self-improving-robotic-agent) - Self-improving generalist robotic agent.
- [SayCan](https://say-can.github.io/) - Grounding language-model planning in affordances for robot tasks.

## Robot Learning

- [DeepMind Control Suite](https://github.com/google-deepmind/dm_control) - Continuous control environments and MuJoCo-based tooling.
- [Diffusion Policy](https://diffusion-policy.cs.columbia.edu/) - Visuomotor policy learning with action diffusion.
- [Implicit Behavioral Cloning](https://implicitbc.github.io/) - Energy-based imitation learning for contact-rich manipulation.
- [R3M](https://sites.google.com/view/robot-r3m/) - Reusable visual representations for robotic manipulation.
- [VC-1](https://github.com/facebookresearch/eai-vc) - Visual representations for embodied AI.
- [DrQ-v2](https://github.com/facebookresearch/drqv2) - Data-regularized reinforcement learning for continuous control.

## Manipulation

- [ALOHA](https://tonyzhaozh.github.io/aloha/) - Low-cost bimanual teleoperation platform and imitation-learning system.
- [ACT](https://tonyzhaozh.github.io/act/) - Action Chunking with Transformers for real-world manipulation.
- [Dex-Net](https://berkeleyautomation.github.io/dex-net/) - Dataset, models, and planning tools for robotic grasping.
- [Transporter Networks](https://transporternets.github.io/) - Keypoint-based rearrangement and manipulation.
- [CLIPort](https://cliport.github.io/) - Language-conditioned tabletop manipulation using semantic priors.

## Navigation and Embodied AI

- [Vision-and-Language Navigation](https://bringmeaspoon.org/) - Room-to-Room benchmark for language-guided navigation.
- [ObjectNav](https://aihabitat.org/challenge/2023/) - Object-goal navigation challenges and baselines.
- [SoundSpaces](https://soundspaces.org/) - Audio-visual embodied AI environments.
- [ALFRED](https://askforalfred.com/) - Language-guided household task benchmark.
- [TEACh](https://teachingalfred.github.io/) - Task-driven embodied agents that communicate with humans.

## Locomotion

- [Legged Gym](https://github.com/leggedrobotics/legged_gym) - GPU-accelerated reinforcement learning for legged robots.
- [Isaac Lab](https://isaac-sim.github.io/IsaacLab/) - Robot learning framework built on NVIDIA Isaac Sim.
- [DeepMimic](https://xbpeng.github.io/projects/DeepMimic/) - Motion imitation with reinforcement learning.
- [AMP](https://xbpeng.github.io/projects/AMP/) - Adversarial motion priors for physics-based character control.

## Simulation and Digital Twins

- [MuJoCo](https://mujoco.org/) - Physics engine for robotics, biomechanics, and control.
- [NVIDIA Isaac Sim](https://developer.nvidia.com/isaac-sim) - Robotics simulation and synthetic-data platform.
- [PyBullet](https://pybullet.org/) - Python robotics and physics simulation.
- [Gazebo](https://gazebosim.org/) - Open-source robotics simulation ecosystem.
- [SAPIEN](https://sapien.ucsd.edu/) - Realistic and interactive simulation for embodied AI.
- [Genesis](https://genesis-embodied-ai.github.io/) - Generative simulation platform for embodied AI.

## Datasets

- [Open X-Embodiment Dataset](https://robotics-transformer-x.github.io/) - Large-scale cross-robot dataset for generalist robot policies.
- [DROID](https://droid-dataset.github.io/) - Distributed robot interaction dataset for imitation learning.
- [BridgeData V2](https://rail-berkeley.github.io/bridgedata/) - Large-scale robot manipulation dataset.
- [RoboNet](https://www.robonet.wiki/) - Multi-robot video dataset for robot learning.
- [Ego4D](https://ego4d-data.org/) - Egocentric perception dataset useful for embodied understanding.
- [Something-Something](https://developer.qualcomm.com/software/ai-datasets/something-something) - Human-object interaction videos for action understanding.

## Tooling

- [ROS 2](https://docs.ros.org/) - Robot operating middleware.
- [MoveIt](https://moveit.ai/) - Motion planning, manipulation, and control framework.
- [Open3D](https://www.open3d.org/) - 3D data processing library.
- [MinkowskiEngine](https://github.com/NVIDIA/MinkowskiEngine) - Sparse convolution library for 3D perception.
- [rerun](https://www.rerun.io/) - Visualization tools for robotics and spatial AI.
- [Weights & Biases](https://wandb.ai/site) - Experiment tracking often used for robot learning.

## Contributing

Contributions are welcome. Please keep entries specific to embodied intelligence,
robot learning, robotics, embodied AI, or interactive agents. Prefer stable project
pages, papers, or repositories over short-lived announcements.