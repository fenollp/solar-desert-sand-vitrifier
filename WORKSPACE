workspace(name = "voidstar")

load("@bazel_tools//tools/build_defs/repo:http.bzl", "http_archive")

http_archive(
    name = "bazel_upgradable",
    strip_prefix = "bazel_upgradable-0.2.1",
    url = "https://github.com/fenollp/bazel_upgradable/archive/0.2.1.zip",
)

load("@bazel_upgradable//:rule.bzl", "upgradable_repository")

upgradable_repository(
    name = "rules_cc",
    branch = "main",
    remote = "git://github.com/bazelbuild/rules_cc.git",
)

# https://mujoco.org/download
http_archive(
    name = "mujoco_linux",
    url = "https://mujoco.org/download/mujoco210-linux-x86_64.tar.gz",
)


# ln -s ~/.mujoco/210 ~/.mujoco/mjpro150
# touch /home/pete/.mujoco/mjkey.txt
# export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/home/pete/.mujoco/mjpro150/bin
# pip3 install gym[mujoco] https://github.com/openai/gym/pull/1731
# pip3 install gym[mujoco] 'mujoco_py==2.1.2.14'
# actually: install gym (>=0.21.0)
# then install mujoco_py >=2.1.2.14
# then dont install gym[mujoco]. you're done...


# pip3 install -U 'mujoco-py<2.2,>=2.1'
# export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/home/pete/.mujoco/mujoco210/bin
# sudo apt install patchelf libosmesa6-dev
# python3 -c "import mujoco_py"
# python3
# >>> model = mujoco_py.load_model_from_path("cdpr.xml")
# >>> sim = mujoco_py.MjSim(model)
# >>> print(sim.data.qpos)
# [ 0.   0.   2.   0.5  0.5 -0.5  0.5]
# >>> sim.data.qpos
# array([ 0. ,  0. ,  2. ,  0.5,  0.5, -0.5,  0.5])
# >>> sim.step()
# >>> sim.data.qpos

# https://github.com/DLR-RM/stable-baselines3#example
# https://github.com/openai/gym/wiki/FAQ#how-do-i-export-the-run-to-a-video-file
