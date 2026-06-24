# Awesome Embodied Intelligence

> A daily updated awesome list for embodied intelligence, collecting papers,
> benchmarks, datasets, simulators, models, and tools for agents that perceive,
> reason, learn, and act through physical or simulated bodies.

Website: <https://evanlyu732.github.io/cursor/>

Embodied intelligence spans robot learning, embodied AI, manipulation, locomotion,
navigation, simulation, vision-language-action models, and world models for
interactive agents that connect perception to action.

## Contents

| Hot | Latest | Core |
| --- | --- | --- |
| [Hot picks](#hottest-papers) | [Recent papers](#recent-papers) | [Surveys](#surveys-and-reading-lists) |
| [Benchmarks](#benchmarks-and-environments) | [Models](#foundation-models-for-action) | [Robot learning](#robot-learning) |
| [Manipulation](#manipulation) | [Navigation](#navigation-and-embodied-ai) | [Locomotion](#locomotion) |
| [Simulation](#simulation-and-digital-twins) | [Datasets](#datasets) | [Tools](#tooling) |

## Hottest Papers

This section highlights the best recent picks from the 10-day paper window.
It is updated automatically using a transparent heuristic based on recency and
embodied-intelligence signals such as VLA, robot foundation models,
manipulation, benchmarks, datasets, safety, and world models. Link shortcuts
search for author sites, X discussion, and Reddit discussion.

<!-- BEGIN AUTO-GENERATED: hottest-papers -->
Last updated: 2026-06-24 UTC
Selected from papers published from 2026-06-15 through 2026-06-24.

| Paper | Why it is hot | Published |
| --- | --- | --- |
| [LIBERO-Safety: A Comprehensive Benchmark for Physical and Semantic Safety in Vision-Language-Action Models](https://arxiv.org/abs/2606.23686) | Vision-language-action, Robot foundation models, Manipulation | 2026-06-22 |
| [dVLA-RL: Reinforcement Learning over Denoising Trajectories for Discrete Diffusion Vision-Language-Action Models](https://arxiv.org/abs/2606.23623) | Vision-language-action, Robot foundation models, Robot learning | 2026-06-22 |
| [BiliVLA: Scene-Aware Vision-Language-Action Model with Reinforcement Learning for Autonomous Biliary Endoscopic Navigation](https://arxiv.org/abs/2606.23531) | Vision-language-action, Robot foundation models, Robot learning | 2026-06-22 |
| [IOI: Decoupling Kinematics and Physics for Interactive World Models](https://arxiv.org/abs/2606.23296) | Robot foundation models, Robot learning, Benchmarks and datasets | 2026-06-22 |
| [PolicyTrim: Boosting Intrinsic Policy Efficiency of Vision-Language-Action Models](https://arxiv.org/abs/2606.22540) | Vision-language-action, Robot foundation models, Robot learning | 2026-06-21 |
<!-- END AUTO-GENERATED: hottest-papers -->

## Recent Papers

This section is updated automatically every day at 08:00 UTC by
[`scripts/update_recent.py`](scripts/update_recent.py). The updater fetches
recent arXiv entries related to embodied intelligence, robot learning,
embodied AI, and vision-language-action systems, keeping papers published in
the last 10 days. Link shortcuts search for author sites, X discussion, and
Reddit discussion.

<!-- BEGIN AUTO-GENERATED: recent-papers -->
Last updated: 2026-06-24 UTC
Showing papers published from 2026-06-15 through 2026-06-24.

| Paper | Authors | Published |
| --- | --- | --- |
| [World Value Models for Robotic Manipulation](https://arxiv.org/abs/2606.24742) | Zhihao Wang, Jianxiong Li, Yu Cui, Yuan Gao, Xianyuan Zhan, Junzhi Yu, et al. (+1) | 2026-06-23 |
| [Supervise What Survives: Geometry-Guided VLA Adaptation from Synthetic Robot Videos](https://arxiv.org/abs/2606.24448) | Danze Chen, Yanzhe Chen, Qiming Huang, Zhijun Cao, Chen Gao, Mike Zheng Shou | 2026-06-23 |
| [SPACE: Enabling Learning from Cross-Robot Data Toward Generalist Policies](https://arxiv.org/abs/2606.24049) | Haeone Lee, Byeongguk Jeon, Suchae Jeong, Jian Kim, Kimin Lee | 2026-06-23 |
| [MANGO: Automated Multi-Agent Test Oracle Generation for Vision-Language-Action Models](https://arxiv.org/abs/2606.24815) | Pablo Valle, Shaukat Ali, Aitor Arrieta, Lionel Briand | 2026-06-23 |
| [InSight: Self-Guided Skill Acquisition via Steerable VLAs](https://arxiv.org/abs/2606.24884) | Maggie Wang, Lars Osterberg, Stephen Tian, Ola Shorinwa, Jiajun Wu, Mac Schwager | 2026-06-23 |
| [G$^3$VLA: Geometric inductive bias for Vision-Language-Action Models](https://arxiv.org/abs/2606.24472) | Yue Peng, Yongzhe Zhao, Artur Habuda, Khuyen Pham, Yanheng Zhu, Tran Nguyen Le, et al. (+2) | 2026-06-23 |
| [Enabling Robust Cloth Manipulation via Inference-Time Simulator-in-the-Loop Refinement](https://arxiv.org/abs/2606.24552) | Xin Liu, Yulin Li, Ziming Li, Pengyu Jing, Zhenhao Huang, Bingyang Zhou, et al. (+4) | 2026-06-23 |
| [DriveStack-VLA: Render-Teacher Alignment for BEV-Based DeepStack Vision-Language-Action Model](https://arxiv.org/abs/2606.24051) | Jingke Wang, Zhenru Zhao, Shuangming Lei, Hao Su, Yuehao Huang, Yijia Xie, et al. (+5) | 2026-06-23 |
| [Compact Object-Level Representations with Open-Vocabulary Understanding for Indoor Visual Relocalization](https://arxiv.org/abs/2606.24767) | Zhaopeng Cui, Jiarui Hu, Jingbo Liu, Boming Zhao, Xiyue Guo, Boyin Feng, et al. (+4) | 2026-06-23 |
| [Beyond Monotonic Progress: Retry-Supervised Value Learning for Robot Imitation](https://arxiv.org/abs/2606.24633) | Xinyao Qin, Junjie Lu, Kaixin Wang, Chuheng Zhang, Sinjae Kang, Kimin Lee, et al. (+4) | 2026-06-23 |
| [AutoSpec: Safety Rule Evolution for LLM Agents via Inductive Logic Programming](https://arxiv.org/abs/2606.24245) | Pingchuan Ma, Zhaoyu Wang, Zimo Ji, Yuguang Zhou, Zhantong Xue, Zongjie Li, et al. (+2) | 2026-06-23 |
| [ArtiTwinSplat: Interactable Digital Twin Reconstruction via Gaussian Splatting from RGB-D videos](https://arxiv.org/abs/2606.24628) | Pranjal Mishra, René Zurbrügg, Max Wilder-Smith, Marco Hutter, Marc Pollefeys, Zuria Bauer, et al. (+1) | 2026-06-23 |
| [Verifiable Foundation Models for Robot Safety](https://arxiv.org/abs/2606.23754) | Davide Corsi, Kyungmin Kim, Roy Fox | 2026-06-22 |
| [UniFS: Unified Fast-to-Slow Hierarchical Architecture for Vision-Language-Action Models](https://arxiv.org/abs/2606.22794) | Lin Sun, Zhiwei Guan, Conglin Wang, Zihong Chen, Jianhai Yu, Zongsheng Li, et al. (+4) | 2026-06-22 |
| [TSD: A Physics-Inspired Trajectory Saliency Detector for Efficient Imitation Learning](https://arxiv.org/abs/2606.23371) | Yiming Zhao, Gongrui Ma, Qingkai Li, Mingguo Zhao | 2026-06-22 |
| [Temporal Logic Guidance for Action-Only Diffusion Policies with World Models](https://arxiv.org/abs/2606.22729) | Moritz Zoellner, Anastasios Manganaris, Rohan Paleja | 2026-06-22 |
| [RECALL: Recovery Experience Collection for Active Lifelong Learning in Vision-Language-Action Models](https://arxiv.org/abs/2606.23617) | Ulas Berk Karli, Tesca Fitzgerald | 2026-06-22 |
| [REALM: A Unified Red-Teaming Benchmark for Physical-World VLMs](https://arxiv.org/abs/2606.23892) | Yifei Zhao, Qian Lou, Mengxin Zheng | 2026-06-22 |
| [P-JEPA: Procedural Video Representation Learning via Joint Embedding Predictive Architecture](https://arxiv.org/abs/2606.23256) | Felix Tristram, Stefano Gasperini, Benjamin Killeen, Marcel Walch, Christian Benz, Nassir Navab, et al. (+1) | 2026-06-22 |
| [LIBERO-Safety: A Comprehensive Benchmark for Physical and Semantic Safety in Vision-Language-Action Models](https://arxiv.org/abs/2606.23686) | Rongxu Cui, Zongzheng Zhang, Jingrui Pang, Haohan Chi, Jinbang Guo, Saining Zhang, et al. (+8) | 2026-06-22 |
| [LaST-HD: Learning Latent Physical Reasoning from Scalable Human Data for Robot Manipulation](https://arxiv.org/abs/2606.23685) | Jiaming Liu, Yinxi Wang, Chenyang Gu, Siyuan Qian, Xiangju Mi, Hao Chen, et al. (+12) | 2026-06-22 |
| [KEMO: Event-Driven Keyframe Memory for Long-Horizon Robot Manipulation with VLA Policies](https://arxiv.org/abs/2606.23589) | Yihan Zeng, Minghao Ye, Yiyuan Chen, Yide Shentu, Philipp Wu, Zike Yan, et al. (+1) | 2026-06-22 |
| [IOI: Decoupling Kinematics and Physics for Interactive World Models](https://arxiv.org/abs/2606.23296) | Chengyu Bai, Peidong Jia, Tiecheng Guo, Yukai Wang, Rui Ma, Fangyuan Zhao, et al. (+8) | 2026-06-22 |
| [Intend, Reflect, Refine: An Adaptive Multimodal Reflection Framework for Autonomous Driving](https://arxiv.org/abs/2606.22913) | Zisheng Chen, Yuping Qiu, Jianhua Han, Tao Tang, Xiuwei Chen, Likui Zhang, et al. (+3) | 2026-06-22 |
| [Improving Robotic Imitation Learning via Trajectory Standardization](https://arxiv.org/abs/2606.22907) | Licheng Yang, Lingfeng Qian, Fei Zheng, Yonghao He, Wei Sui, Shuangshuang Li, et al. (+1) | 2026-06-22 |
| [IMAGIN-4D: Image-Guided Controllable Interaction Generation](https://arxiv.org/abs/2606.23675) | Sai Kumar Dwivedi, Federica Bogo, Buğra Tekin, Chenhongyi Yang, Nadine Bertsch, Tomas Hodan, et al. (+3) | 2026-06-22 |
| [Humanoid-OmniOcc: Stereo-Based Full-View Occupancy Dataset for Embodied AI](https://arxiv.org/abs/2606.22971) | Xianda Guo, Bohao Zhang, Chenwei Huang, Shiyuan Chen, Ruilin Wang, Yiqun Duan, et al. (+3) | 2026-06-22 |
| [HoloAgent-0: A Unified Embodied Agent Framework with 3D Spatial Memory](https://arxiv.org/abs/2606.23565) | Xiaolin Zhou, Liu Liu, Tingyang Xiao, Wei Feng, Fa Fu, Xinrui Meng, et al. (+6) | 2026-06-22 |
| [HiL-ResRL: A Model-Agnostic Finetuning Adapter via Human-in-the-loop Residual Reinforcement Learning](https://arxiv.org/abs/2606.22860) | Jingyi Liu, Zhaohong Mai, ShunSen He, Hang Ren, Chao Wang, Shunbo Zhou, et al. (+2) | 2026-06-22 |
| [Foresight: Failure Detection for Long-Horizon Robotic Manipulation with Action-Conditioned World Model Latents](https://arxiv.org/abs/2606.23085) | Haoran Zhang, Yifu Lu, Boyang Wang, Xuhui Kang, Yen-Ling Kuo, Zezhou Cheng, et al. (+2) | 2026-06-22 |
| [Flowing With Purpose: Latent Action Guided Flow Matching Policies For Robotic Manipulation](https://arxiv.org/abs/2606.23420) | Bruno Machado, Alexandre Chapin, Emmanuel Dellandrea, Liming Chen | 2026-06-22 |
| [Flow6D: Discrete-to-Continuous Flow Matching for Efficient and Accurate Category-Level 6D Pose Estimation](https://arxiv.org/abs/2606.23293) | Mingyu Mei, Li Zhang, Zibo Dai, Han Sun, Xinyue Zhao, Huiliang Shen, et al. (+1) | 2026-06-22 |
| [Flow as Flow: Modeling Robot Velocity Fields as Probability Velocity Fields for Flow-Based Object Manipulation](https://arxiv.org/abs/2606.23090) | Koki Seno, Daichi Yashima, Yusuke Takagi, Kento Tokura, Komei Sugiura | 2026-06-22 |
| [Flatness Preserves Instruction Following in Vision-Language-Action Models](https://arxiv.org/abs/2606.23641) | Haochen Zhang, Yonatan Bisk | 2026-06-22 |
| [dVLA-RL: Reinforcement Learning over Denoising Trajectories for Discrete Diffusion Vision-Language-Action Models](https://arxiv.org/abs/2606.23623) | Yuhao Wu, Yitian Liu, Weijie Shen, Mishuo Han, Wenjie Xu, Haotian Liang, et al. (+10) | 2026-06-22 |
| [Cloak: Zero-Shot Cross-Embodiment Manipulation by Masking the End-Effector from the VLA](https://arxiv.org/abs/2606.22836) | Michael Piseno, Guy Tevet, C. Karen Liu | 2026-06-22 |
| [Bridging Semantics and Kinematics: A Modular Framework for Zero-Shot Robotic Manipulation](https://arxiv.org/abs/2606.23157) | Ali Alabbas, Dipshikha Das, Camillo Murgia, Sainul Ansary, Alaa Elkamash, Philip Long | 2026-06-22 |
| [BiliVLA: Scene-Aware Vision-Language-Action Model with Reinforcement Learning for Autonomous Biliary Endoscopic Navigation](https://arxiv.org/abs/2606.23531) | Jinsong Lin, Chi kit Ng, Zhiyong Xiong, Zikang Pan, Yihan Hu, Tabassum Tamima, et al. (+5) | 2026-06-22 |
| [Attacking the Trusted Imagination: Oracle-Level Integrity Attacks on Imagine-then-Act World Models](https://arxiv.org/abs/2606.22966) | Linghan Chen, Kaiyan Ji, Minyu Guo | 2026-06-22 |
| [Assistron: Bayesian Shared Autonomy with Off-the-shelf Vision-Language-Action Models](https://arxiv.org/abs/2606.23147) | Pinhao Song, Ze Fu, Yutong Hu, Renaud Detry | 2026-06-22 |
| [AdaReP:Adaptive Re-Planning under Model Mismatch for Neural World-Model Predictive Control](https://arxiv.org/abs/2606.23079) | Yutian Cheng, Xiaojian Ma, Xianhao Wang, Min Yang, Rongpeng Su, Hangxin Liu, et al. (+3) | 2026-06-22 |
| [A Watermark for Vision-Language-Action and World Action Models](https://arxiv.org/abs/2606.23574) | Yule Liu, Shuai Liu, Jiaheng Wei, Xinlei He | 2026-06-22 |
| [Tactile Genesis: Exploring Tactile Sensors at Scale for Learning Dexterous Tasks](https://arxiv.org/abs/2606.22332) | Trinity Chung, Kashu Yamazaki, Dhruv Patel, Alexis Duburcq, Yiling Qiao, Katerina Fragkiadaki, et al. (+1) | 2026-06-21 |
| [Self-Evolving Cognitive Framework via Causal World Modeling for Embodied Scientific Intelligence](https://arxiv.org/abs/2606.22449) | Yi Yu, Tetsunari Inamura | 2026-06-21 |
| [PolicyTrim: Boosting Intrinsic Policy Efficiency of Vision-Language-Action Models](https://arxiv.org/abs/2606.22540) | Xianghui Wang, Feng Chen, Wenbo Zhang, Hua Yan, Zixuan Wang, Changsheng Li, et al. (+1) | 2026-06-21 |
| [FlowDPG: Deterministic Policy Gradient on Flow Matching Policies for Real-World Manipulation](https://arxiv.org/abs/2606.22303) | Kexin Shi, Junyao Shi, Poorvi Hebbar, Zhuolun Zhao, Tarun Amarnath, Yifan Su, et al. (+2) | 2026-06-21 |
| [Do Rigid-Body Simulators Dream of Soft Robots? Learning Contact-Rich Manipulation for Tendon-Driven Continuum Robots](https://arxiv.org/abs/2606.22397) | Chengnan Shentu, Nicholas Baldassini, Tongjia Zheng, Priyanka Rao, Jessica Burgner-Kahrs | 2026-06-21 |
| [ARP: Enhancing Quantized Skill Abstractions via Visual Alignment and Iterative Refinement for Robotic Manipulation](https://arxiv.org/abs/2606.22480) | Yuntian Wang, Zesheng Jia, Yuhui Duan, Qibing Wang, Yang Liu, Song Wang, et al. (+2) | 2026-06-21 |
| [Any-Body Guard: Universal Safeguarding for Manipulation Policies via Action Masking](https://arxiv.org/abs/2606.22278) | Alex Beaudin, Hanna Krasowski, Kartik Nagpal, Sanjit A. Seshia, Murat Arcak, Negar Mehr | 2026-06-21 |
| [RoboLineage: Agent-Native Data Lifecycle Governance Across Robot Policy Iterations](https://arxiv.org/abs/2606.22142) | Qian Luo, Wentao Guo, Zhennan Qin, Nanchun Guo, Yunhan Zhao, Yi Ma, et al. (+1) | 2026-06-20 |
| [RARM: Confidence-Gated Progress Reward Modeling for RL in Manipulation](https://arxiv.org/abs/2606.22027) | Pengzhi Yang, Xinyu Wang, Pengyu Jing, Kehan Wen, Yiduo Qu, Zhenhao Huang, et al. (+4) | 2026-06-20 |
| [OpenHLM: An Empirical Recipe for Whole-Body Humanoid Loco-Manipulation](https://arxiv.org/abs/2606.22174) | Yingdong Hu, Haodong Zhu, Boyuan Zheng, Yihang Hu, Tong Zhang, Zunhao Chen, et al. (+3) | 2026-06-20 |
| [How Should a Simulation-to-Reality Transfer Budget Be Spent?](https://arxiv.org/abs/2606.22062) | Syed Hamzah Rizvi, Yash Vardhan Tomar | 2026-06-20 |
| [DeformX: A Versatile Co-Simulation Framework for Deformable Linear Objects](https://arxiv.org/abs/2606.22116) | Yi Yang, Xiang Fei, Lehong Wang, Chenhao Li, Zilin Dai, Henry Kou, et al. (+2) | 2026-06-20 |
| [CoRDE: Concept-Prior Routed Diffusion Experts for Structural Generalization in Robot Manipulation](https://arxiv.org/abs/2606.21935) | Haidong Huang, Xixin Zhao, Yaohua Zhou, Jiayu Song, Jiayi Zhang, Jun Ma, et al. (+2) | 2026-06-20 |
| [VQActFlow: Vector-Quantized Action Mode Steering for Multi-Task Robot Manipulation](https://arxiv.org/abs/2606.21600) | Zhigen Zhao, Mark Leggiero, Yipu Chen, Haoran Liu, Yifan Wu, Huishu Xue, et al. (+2) | 2026-06-19 |
| [UniviewVLA: A Unified Multiview Vision-Language-Action Model with World Modeling](https://arxiv.org/abs/2606.21501) | Tao Xu, Runhao Zhang, Zhijian Huang, Jiayi Guan, Jiaxin Wang, Yifan Ding, et al. (+4) | 2026-06-19 |
| [Robot Self-Improvement via Human-Video Dynamics Models](https://arxiv.org/abs/2606.21406) | Hanzhi Chen, Anran Zhang, Simon Schaefer, Kejia Chen, Shi Chen, Daniel Cremers, et al. (+2) | 2026-06-19 |
| [LK Jam: System Architecture and Implementation of a Real-Time Human-AI Interactive Music Generation System using Role-Aware GRU](https://arxiv.org/abs/2606.21018) | Yakun Liu, Zhiyu Jin, Dong Liu, Hai Luan | 2026-06-19 |
| [Inductive Generalization for Robotic Manipulation](https://arxiv.org/abs/2606.20999) | Annabella Macaluso, Haochen Zhang, Ishaan Masilamony, Yingshan Chang, Yonatan Bisk | 2026-06-19 |
| [Decoupling the Declarative from the Procedural in Vision-Language-Action Models](https://arxiv.org/abs/2606.21496) | Nikolaos Tsagkas, Andreas Sochopoulos, Chris Xiaoxuan Lu, Oisin Mac Aodha, Alexandros Kouris | 2026-06-19 |
| [A DVDrive Approach for doScenes Instructed Driving Challenge](https://arxiv.org/abs/2606.21623) | Zijian Fu, Xiangyang Chu, Mengshi Qi, Huadong Ma, Guanghao Zhang, Wei Li | 2026-06-19 |
| [SignVLA: Real-Time Sign Language-Guided Robotic Manipulation via Attention LSTM and Vision-Language-Action Models](https://arxiv.org/abs/2606.20857) | Ningwei Bai, Xinyu Tan, Harry Gardner, Zhengyang Zhong, Liuhaichen Yang, Luoyu Zhang, et al. (+3) | 2026-06-18 |
| [See-and-Reach: Precise Vision-Language Navigation for UAVs within the Field of View](https://arxiv.org/abs/2606.20045) | Fanfu Xue, En Yu, Yantian Shen, Zhikun Hu, Hongjun Wang, Yang Yang, et al. (+2) | 2026-06-18 |
| [Occ-VLM: Occupancy Grounded Vision Language Model for Indoor Scene Understanding](https://arxiv.org/abs/2606.19776) | Jianing Li, Zhou Fang, Yijiang Liu, Li Du | 2026-06-18 |
| [Generating Robot Hands from Human Demonstrations](https://arxiv.org/abs/2606.20549) | Sha Yi, Nicklas Hansen, Xueqian Bai, Carmelo Sferrazza, Michael T. Tolley, Xiaolong Wang | 2026-06-18 |
| [Finetuning Vision-Language-Action Models Requires Fewer Layers Than You Think](https://arxiv.org/abs/2606.20246) | Gia-Binh Nguyen, Trong-Bao Ho, Thien-Loc Ha, Khoa Vo, Philip Lund Møller, Quang T. Nguyen, et al. (+15) | 2026-06-18 |
| [EquiVLA: A General Framework for Rotationally Equivariant Vision-Language-Action Models](https://arxiv.org/abs/2606.19784) | Thien-Loc Ha, Quang-Tan Nguyen, Trong-Bao Ho, Long Dinh, Minh Duc Nguyen, Gia-Binh Nguyen, et al. (+5) | 2026-06-18 |
| [Duet: Dual-Robot Understanding via Efficient Teaching](https://arxiv.org/abs/2606.20990) | Yiqi Zhao, Ruohai Ge, Celina Shiyu Wang, Junjie Ye, Muchen Xu, Minhao Li, et al. (+7) | 2026-06-18 |
| [CoLI: A Reproducible Platform for Continuum Robot Learning via Monolithic 3D Printing and Isomorphic Teleoperation](https://arxiv.org/abs/2606.20389) | Ziyuan Tang, Chenxi Xiao* | 2026-06-18 |
| [Advancing DialNav through Automatic Embodied Dialog Augmentation](https://arxiv.org/abs/2606.19948) | Leekyeung Han, Sangwon Jung, Hyunji Min, Jinseong Jeong, Minyoung Kim, Paul Hongsuck Seo | 2026-06-18 |
| [A Measurement Study of Cryptographic Misuse in Embodied AI Mobile Applications](https://arxiv.org/abs/2606.19983) | Junchao Li, Xuelei Wang, Yuhang Huang, Qi Wang, Boyang Ma, Xuelong Dai, et al. (+2) | 2026-06-18 |
| [WorldLines: Benchmarking and Modeling Long-Horizon Stateful Embodied Agents](https://arxiv.org/abs/2606.18847) | Yehang Zhang, Jianchong Su, Haojian Huang, Yifan Chang, Tianhao Zhou, Xinli Xu, et al. (+4) | 2026-06-17 |
| [TactSpace: Learning a Physics-enriched Shared Latent Space for Tactile Sim-to-Real Transfer](https://arxiv.org/abs/2606.18959) | Arunim Joarder, Arjun Bhardwaj, René Zurbrügg, Mayank Mittal, Florin Püntener, Sira Bielefeldt, et al. (+3) | 2026-06-17 |
| [SC3-Eval: Evaluating Robot Foundation Models via Self-Consistent Video Generation](https://arxiv.org/abs/2606.18610) | Wei-Cheng Tseng, Gashon Hussein, Yuzhu Dong, Allen Z. Ren, Lucy X. Shi, XuDong Wang, et al. (+6) | 2026-06-17 |
| [Playful Agentic Robot Learning](https://arxiv.org/abs/2606.19419) | Junyi Zhang, Jiaxin Ge, Hanjun Yoo, Letian Fu, Zihan Yang, Yaowei Liu, et al. (+14) | 2026-06-17 |
| [OneCanvas: 3D Scene Understanding via Panoramic Reprojection](https://arxiv.org/abs/2606.19253) | Bartłomiej Baranowski, Dave Zhenyu Chen, Matthias Nießner | 2026-06-17 |
| [One Demo is Worth a Thousand Trajectories: Action-View Augmentation for Visuomotor Policies](https://arxiv.org/abs/2606.19586) | Chuer Pan, Litian Liang, Dominik Bauer, Eric Cousineau, Benjamin Burchfiel, Siyuan Feng, et al. (+1) | 2026-06-17 |
| [Mem-World: Memory-Augmented Action-Conditioned World Models for Persistent Robot Manipulation](https://arxiv.org/abs/2606.18960) | Zirui Zheng, Jiaqian Yu, Xiongfeng Peng, jun shi, Mingyi Li, Chao Zhang, et al. (+4) | 2026-06-17 |
| [Fail-RAG : A Retrieval Augmented Generation Informed Framework for Robot Failure Identification](https://arxiv.org/abs/2606.19598) | Ameya Salvi, Jie Hu | 2026-06-17 |
| [A Scalable Embodied Intelligence Platform for Seamless Real-to-Sim-to-Real Transfer of Household Mobile Manipulation Tasks](https://arxiv.org/abs/2606.18646) | Kui Yang, Xianlei Long, Haoxuan Li, Yan Ding, Chao Chen | 2026-06-17 |
| [When Robots Sleep: Offline Skill Consolidation for Shared-Policy Robot Learning](https://arxiv.org/abs/2606.17493) | Nethmi Jayasinghe, Diana Gontero, Amit Ranjan Trivedi | 2026-06-16 |
| [Visual Verification Enables Inference-time Steering and Autonomous Policy Improvement](https://arxiv.org/abs/2606.18247) | Mingtong Zhang, Dhruv Shah | 2026-06-16 |
| [Memory as a Wasting Asset: Pricing Flash Endurance for Embodied Agents, and the Limits of Doing So](https://arxiv.org/abs/2606.18144) | Josef Liyanjun Chen | 2026-06-16 |
| [MagicSim: A Unified Infrastructure for Executable Embodied Interaction](https://arxiv.org/abs/2606.17511) | Haoran Lu, Songling Liu, Yue Chen, Guo Ye, Mutian Shen, Shuyang Yu, et al. (+12) | 2026-06-16 |
| [Guava: An Effective and Universal Harness for Embodied Manipulation](https://arxiv.org/abs/2606.18363) | Haowen Liu, Xirui Li, Shaoxiong Yao, Peng Shi, Tianyi Zhou, Jia-Bin Huang, et al. (+2) | 2026-06-16 |
| [GASE: Gaussian Splatting-Based Automated System for Reconstructing Embodied-Simulation Environments](https://arxiv.org/abs/2606.17520) | Jiawei Zhang, Yiming Yan, Chao Liang, Nuo Xu, Seson Sun, Qichen Zhang, et al. (+5) | 2026-06-16 |
| [From Ad Hoc Pilots to Repeatable Patterns: Structuring Drone Collaboration in Emergency Services with DroneLets](https://arxiv.org/abs/2606.17839) | Dzmitry Katsiuba, Samuel Brander, Mateusz Dolata, Gerhard Schwabe | 2026-06-16 |
| [EvolveNav: Proactive Preflection and Self-Evolving Memory for Zero-Shot Object Goal Navigation](https://arxiv.org/abs/2606.18235) | Qi Chai, Wenhao Shen, Nanjie Yao, Yue Xia, Kaiyong Zhao, Jie Ma, et al. (+2) | 2026-06-16 |
| [ERQA-Plus: A Diagnostic Benchmark for Reasoning in Embodied AI](https://arxiv.org/abs/2606.17639) | Hong Yang, Basura Fernando | 2026-06-16 |
| [EgoInfinity: A Web-Scale 4D Hand-Object Interaction Data Engine for Any-View Robot Retargeting and Video-to-Action Robot Learning](https://arxiv.org/abs/2606.17385) | Gaotian Wang, Kejia Ren, Andrew Morgan, Yiting Chen, Howard H. Qian, Podshara Chanrungmaneekul, et al. (+1) | 2026-06-16 |
| [DexLink Hand: A Compact, Affordable, 16-DOF Linkage-Driven Hand with Human-Like Dexterity](https://arxiv.org/abs/2606.17418) | Hao Wu, Yanzhe Wang, Yu Feng, Jian Liu, Jihao Li, Jianshu Zhou, et al. (+1) | 2026-06-16 |
| [V2P-Manip: Learning Dexterous Manipulation from Monocular Human Videos](https://arxiv.org/abs/2606.16436) | Kaihan Chen, Yanming Shao, Haifeng Ji, Xiaokang Yang, Yao Mu | 2026-06-15 |
| [Unified Motion-Action Modeling for Heterogeneous Robot Learning](https://arxiv.org/abs/2606.16917) | Yunhao Cao, Shitong Liu, Chao Feng, Meryl Zhang, Xuanchen Lu, Andrew Owens, et al. (+1) | 2026-06-15 |
| [Semantic Flip: Synthetic OOD Generation for Robust Refusal in Embodied Question Answering and Spatial Localization](https://arxiv.org/abs/2606.16898) | Dongbin Na, Chanwoo Kim, Giyun Choi, Dooyoung Hong | 2026-06-15 |
| [SafeDojo: Safe Reinforcement Learning for VLA via Interactive World Model](https://arxiv.org/abs/2606.20698) | Kai Tang, Peidong Jia, Zhong Chu, Jixian Wu, Rui Ma, Jiajun Cao, et al. (+12) | 2026-06-15 |
| [Qwen-RobotWorld Technical Report: Unifying Embodied World Modeling through Language-Conditioned Video Generation](https://arxiv.org/abs/2606.17030) | Jie Zhang, Xiaoyue Chen, Anzhe Chen, Dayiheng Liu, Deqing Li, Gengze Zhou, et al. (+33) | 2026-06-15 |
| [Geometric Action Model for Robot Policy Learning](https://arxiv.org/abs/2606.17046) | Jisang Han, Seonghu Jeon, Jaewoo Jung, René Zurbrügg, Honggyu An, Tifanny Portela, et al. (+4) | 2026-06-15 |
| [DataLadder: A Simulation-Enabled Interconversion Toolchain for the Embodied Data Pyramid](https://arxiv.org/abs/2606.16776) | Peidong Liu, Yongce Liu, Songyan Guo, Fuyuan Ma, Zhihao Yuan, Ao Li, et al. (+25) | 2026-06-15 |
| [An Augmented Reality Brain-Robot Interface for Generalist Robot Arm Manipulation](https://arxiv.org/abs/2606.16413) | Shangkai Zhang, Rousslan Fernand Julien Dossa, Luca Nunziante, Marina Di Vincenzo, Kai Arulkumaran | 2026-06-15 |
| [ActiveSAM: Image-Conditional Class Pruning for Fast and Accurate Open-Vocabulary Segmentation](https://arxiv.org/abs/2606.16996) | Tran Dinh Tien, Zhiqiang Shen | 2026-06-15 |
<!-- END AUTO-GENERATED: recent-papers -->

## Surveys and Reading Lists

| Resource | Description |
| --- | --- |
| [A Survey of Embodied AI](https://arxiv.org/abs/2108.04097) | Overview of embodied AI tasks, simulators, datasets, and evaluation. |
| [Robot Learning: A Review of Methods and Applications](https://arxiv.org/abs/2209.11803) | Broad review of robot learning methods and deployments. |
| [Foundation Models in Robotics: Applications, Challenges and the Future](https://arxiv.org/abs/2312.07843) | Survey of foundation-model use in robotics. |
| [Awesome Robotics Foundation Models](https://github.com/robotics-survey/Awesome-Robotics-Foundation-Models) | Community list focused on foundation models for robotics. |
| [Awesome Embodied AI](https://github.com/HCPLab-SYSU/Awesome-Embodied-AI) | Papers and resources for embodied AI and embodied agents. |

## Benchmarks and Environments

| Resource | Description |
| --- | --- |
| [AI2-THOR](https://ai2thor.allenai.org/) | Interactive 3D environments for visual AI and embodied agents. |
| [Habitat](https://aihabitat.org/) | Platform for embodied AI research in simulation. |
| [ManiSkill](https://maniskill.ai/) | GPU-accelerated benchmark suite for robotic manipulation. |
| [Meta-World](https://meta-world.github.io/) | Multi-task and meta-reinforcement-learning benchmark for manipulation. |
| [robosuite](https://robosuite.ai/) | Modular simulation framework and benchmark suite for robot learning. |
| [RLBench](https://sites.google.com/view/rlbench) | Robot learning benchmark with many manipulation tasks. |
| [BEHAVIOR](https://behavior.stanford.edu/) | Benchmark for household activities in simulation. |
| [iGibson](https://svl.stanford.edu/igibson/) | Interactive simulation environments for embodied AI. |

## Foundation Models for Action

| Resource | Description |
| --- | --- |
| [RT-1](https://robotics-transformer1.github.io/) | Robotics Transformer for real-world robot control from large-scale demonstrations. |
| [RT-2](https://robotics-transformer2.github.io/) | Vision-language-action models that transfer web-scale knowledge to robotic control. |
| [Open X-Embodiment](https://robotics-transformer-x.github.io/) | Cross-embodiment dataset and models for robot learning. |
| [PaLM-E](https://palm-e.github.io/) | Embodied multimodal language model for robotics and vision-language reasoning. |
| [VIMA](https://vimalabs.github.io/) | Multimodal prompting for generalist robot manipulation. |
| [Octo](https://octo-models.github.io/) | Open-source generalist robot policy trained on diverse robot data. |
| [RoboCat](https://www.deepmind.com/blog/robocat-a-self-improving-robotic-agent) | Self-improving generalist robotic agent. |
| [SayCan](https://say-can.github.io/) | Grounding language-model planning in affordances for robot tasks. |

## Robot Learning

| Resource | Description |
| --- | --- |
| [DeepMind Control Suite](https://github.com/google-deepmind/dm_control) | Continuous control environments and MuJoCo-based tooling. |
| [Diffusion Policy](https://diffusion-policy.cs.columbia.edu/) | Visuomotor policy learning with action diffusion. |
| [Implicit Behavioral Cloning](https://implicitbc.github.io/) | Energy-based imitation learning for contact-rich manipulation. |
| [R3M](https://sites.google.com/view/robot-r3m/) | Reusable visual representations for robotic manipulation. |
| [VC-1](https://github.com/facebookresearch/eai-vc) | Visual representations for embodied AI. |
| [DrQ-v2](https://github.com/facebookresearch/drqv2) | Data-regularized reinforcement learning for continuous control. |

## Manipulation

| Resource | Description |
| --- | --- |
| [ALOHA](https://tonyzhaozh.github.io/aloha/) | Low-cost bimanual teleoperation platform and imitation-learning system. |
| [ACT](https://tonyzhaozh.github.io/act/) | Action Chunking with Transformers for real-world manipulation. |
| [Dex-Net](https://berkeleyautomation.github.io/dex-net/) | Dataset, models, and planning tools for robotic grasping. |
| [Transporter Networks](https://transporternets.github.io/) | Keypoint-based rearrangement and manipulation. |
| [CLIPort](https://cliport.github.io/) | Language-conditioned tabletop manipulation using semantic priors. |

## Navigation and Embodied AI

| Resource | Description |
| --- | --- |
| [Vision-and-Language Navigation](https://bringmeaspoon.org/) | Room-to-Room benchmark for language-guided navigation. |
| [ObjectNav](https://aihabitat.org/challenge/2023/) | Object-goal navigation challenges and baselines. |
| [SoundSpaces](https://soundspaces.org/) | Audio-visual embodied AI environments. |
| [ALFRED](https://askforalfred.com/) | Language-guided household task benchmark. |
| [TEACh](https://teachingalfred.github.io/) | Task-driven embodied agents that communicate with humans. |

## Locomotion

| Resource | Description |
| --- | --- |
| [Legged Gym](https://github.com/leggedrobotics/legged_gym) | GPU-accelerated reinforcement learning for legged robots. |
| [Isaac Lab](https://isaac-sim.github.io/IsaacLab/) | Robot learning framework built on NVIDIA Isaac Sim. |
| [DeepMimic](https://xbpeng.github.io/projects/DeepMimic/) | Motion imitation with reinforcement learning. |
| [AMP](https://xbpeng.github.io/projects/AMP/) | Adversarial motion priors for physics-based character control. |

## Simulation and Digital Twins

| Resource | Description |
| --- | --- |
| [MuJoCo](https://mujoco.org/) | Physics engine for robotics, biomechanics, and control. |
| [NVIDIA Isaac Sim](https://developer.nvidia.com/isaac-sim) | Robotics simulation and synthetic-data platform. |
| [PyBullet](https://pybullet.org/) | Python robotics and physics simulation. |
| [Gazebo](https://gazebosim.org/) | Open-source robotics simulation ecosystem. |
| [SAPIEN](https://sapien.ucsd.edu/) | Realistic and interactive simulation for embodied AI. |
| [Genesis](https://genesis-embodied-ai.github.io/) | Generative simulation platform for embodied AI. |

## Datasets

| Resource | Description |
| --- | --- |
| [Open X-Embodiment Dataset](https://robotics-transformer-x.github.io/) | Large-scale cross-robot dataset for generalist robot policies. |
| [DROID](https://droid-dataset.github.io/) | Distributed robot interaction dataset for imitation learning. |
| [BridgeData V2](https://rail-berkeley.github.io/bridgedata/) | Large-scale robot manipulation dataset. |
| [RoboNet](https://www.robonet.wiki/) | Multi-robot video dataset for robot learning. |
| [Ego4D](https://ego4d-data.org/) | Egocentric perception dataset useful for embodied understanding. |
| [Something-Something](https://developer.qualcomm.com/software/ai-datasets/something-something) | Human-object interaction videos for action understanding. |

## Tooling

| Resource | Description |
| --- | --- |
| [ROS 2](https://docs.ros.org/) | Robot operating middleware. |
| [MoveIt](https://moveit.ai/) | Motion planning, manipulation, and control framework. |
| [Open3D](https://www.open3d.org/) | 3D data processing library. |
| [MinkowskiEngine](https://github.com/NVIDIA/MinkowskiEngine) | Sparse convolution library for 3D perception. |
| [rerun](https://www.rerun.io/) | Visualization tools for robotics and spatial AI. |
| [Weights & Biases](https://wandb.ai/site) | Experiment tracking often used for robot learning. |

## Contributing

Contributions are welcome. Please keep entries specific to embodied intelligence,
robot learning, robotics, embodied AI, or interactive agents. Prefer stable project
pages, papers, or repositories over short-lived announcements.
