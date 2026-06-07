#This file is part of lrc2cdg.
#
#lrc2cdg is free software: you can redistribute it and/or modify
#it under the terms of the GNU General Public License as published by
#the Free Software Foundation, either version 3 of the License, or
#(at your option) any later version.
#
#lrc2cdg is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU General Public License for more details.
#
#You should have received a copy of the GNU General Public License
#along with lrc2cdg.  If not, see <https://www.gnu.org/licenses/>.

cmake_minimum_required(VERSION 3.16.0)
set(CMAKE_CXX_STANDARD 20)

set(CMAKE_CXX_FLAGS "-pg -O0 -g3 -Wall -Wpedantic")
set(CMAKE_CXX_COMPILER g++)

project(lrc2cdg LANGUAGES CXX)

add_subdirectory(json)
include_directories(json/include)

set(SOURCE
    lrc2cdg.cpp
)

add_executable(${PROJECT_NAME})
target_sources(${PROJECT_NAME} PRIVATE ${SOURCE})

target_link_libraries(${PROJECT_NAME})