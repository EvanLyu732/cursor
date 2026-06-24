# Awesome Embodied Intelligence

> A daily updated awesome list for embodied intelligence, collecting papers,
> benchmarks, datasets, simulators, models, and tools for agents that perceive,
> reason, learn, and act through physical or simulated bodies.

Website: <https://evanlyu732.github.io/cursor/>

Embodied intelligence spans robot learning, embodied AI, manipulation, locomotion,
navigation, simulation, vision-language-action models, and world models for
interactive agents that connect perception to action.

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

- [World Value Models for Robotic Manipulation](https://arxiv.org/abs/2606.24742) - Zhihao Wang, Jianxiong Li, Yu Cui, Yuan Gao, Xianyuan Zhan, Junzhi Yu, et al. (+1) (2026-06-23)
- [Supervise What Survives: Geometry-Guided VLA Adaptation from Synthetic Robot Videos](https://arxiv.org/abs/2606.24448) - Danze Chen, Yanzhe Chen, Qiming Huang, Zhijun Cao, Chen Gao, Mike Zheng Shou (2026-06-23)
- [SPACE: Enabling Learning from Cross-Robot Data Toward Generalist Policies](https://arxiv.org/abs/2606.24049) - Haeone Lee, Byeongguk Jeon, Suchae Jeong, Jian Kim, Kimin Lee (2026-06-23)
- [MANGO: Automated Multi-Agent Test Oracle Generation for Vision-Language-Action Models](https://arxiv.org/abs/2606.24815) - Pablo Valle, Shaukat Ali, Aitor Arrieta, Lionel Briand (2026-06-23)
- [InSight: Self-Guided Skill Acquisition via Steerable VLAs](https://arxiv.org/abs/2606.24884) - Maggie Wang, Lars Osterberg, Stephen Tian, Ola Shorinwa, Jiajun Wu, Mac Schwager (2026-06-23)
- [G$^3$VLA: Geometric inductive bias for Vision-Language-Action Models](https://arxiv.org/abs/2606.24472) - Yue Peng, Yongzhe Zhao, Artur Habuda, Khuyen Pham, Yanheng Zhu, Tran Nguyen Le, et al. (+2) (2026-06-23)
- [Enabling Robust Cloth Manipulation via Inference-Time Simulator-in-the-Loop Refinement](https://arxiv.org/abs/2606.24552) - Xin Liu, Yulin Li, Ziming Li, Pengyu Jing, Zhenhao Huang, Bingyang Zhou, et al. (+4) (2026-06-23)
- [DriveStack-VLA: Render-Teacher Alignment for BEV-Based DeepStack Vision-Language-Action Model](https://arxiv.org/abs/2606.24051) - Jingke Wang, Zhenru Zhao, Shuangming Lei, Hao Su, Yuehao Huang, Yijia Xie, et al. (+5) (2026-06-23)
- [Compact Object-Level Representations with Open-Vocabulary Understanding for Indoor Visual Relocalization](https://arxiv.org/abs/2606.24767) - Zhaopeng Cui, Jiarui Hu, Jingbo Liu, Boming Zhao, Xiyue Guo, Boyin Feng, et al. (+4) (2026-06-23)
- [Beyond Monotonic Progress: Retry-Supervised Value Learning for Robot Imitation](https://arxiv.org/abs/2606.24633) - Xinyao Qin, Junjie Lu, Kaixin Wang, Chuheng Zhang, Sinjae Kang, Kimin Lee, et al. (+4) (2026-06-23)
- [AutoSpec: Safety Rule Evolution for LLM Agents via Inductive Logic Programming](https://arxiv.org/abs/2606.24245) - Pingchuan Ma, Zhaoyu Wang, Zimo Ji, Yuguang Zhou, Zhantong Xue, Zongjie Li, et al. (+2) (2026-06-23)
- [ArtiTwinSplat: Interactable Digital Twin Reconstruction via Gaussian Splatting from RGB-D videos](https://arxiv.org/abs/2606.24628) - Pranjal Mishra, René Zurbrügg, Max Wilder-Smith, Marco Hutter, Marc Pollefeys, Zuria Bauer, et al. (+1) (2026-06-23)
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