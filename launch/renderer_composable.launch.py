# -----------------------------------------------------------------------------
# Copyright 2021 Bernd Pfrommer <bernd.pfrommer@gmail.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
#

import launch
from launch_ros.actions import ComposableNodeContainer
from launch_ros.descriptions import ComposableNode
from launch.substitutions import LaunchConfiguration as LaunchConfig
from launch.actions import DeclareLaunchArgument as LaunchArg
from launch.actions import OpaqueFunction


def launch_setup(context, *args, **kwargs):
    """Create composable node."""
    cam_name = LaunchConfig("camera_name")
    cam_str = cam_name.perform(context)
    container = ComposableNodeContainer(
        name="event_renderer",
        namespace="",
        package="rclcpp_components",
        executable="component_container",
        composable_node_descriptions=[
            ComposableNode(
                package="event_camera_renderer",
                plugin="event_camera_renderer::Renderer",
                name=cam_str + "_renderer",
                parameters=[{"fps": 25.0}],
                remappings=[("~/events", cam_str + "/events")],
                extra_arguments=[{"use_intra_process_comms": True}],
            )
        ],
        output="screen",
    )
    return [container]


def generate_launch_description():
    """Create composable node by calling opaque function."""
    return launch.LaunchDescription(
        [
            LaunchArg("camera_name", default_value=["event_camera"], description="camera name"),
            OpaqueFunction(function=launch_setup),
        ]
    )
