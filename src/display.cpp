// -*-c++-*---------------------------------------------------------------------------------------
// Copyright 2022 Bernd Pfrommer <bernd.pfrommer@gmail.com>
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//     http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

#include "event_camera_renderer/display.h"

#include "event_camera_renderer/sharp_display.h"
#include "event_camera_renderer/time_slice_display.h"

namespace event_camera_renderer
{
std::shared_ptr<Display> Display::newInstance(const std::string & type)
{
  if (type == "time_slice") {
    return (std::make_shared<TimeSliceDisplay>());

  } else if (type == "sharp") {
    return (std::make_shared<SharpDisplay>());
  }
  return (0);
}
}  // namespace event_camera_renderer
