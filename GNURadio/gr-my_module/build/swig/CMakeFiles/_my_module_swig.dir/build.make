# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.14

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:


#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:


# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list


# Suppress display of executed commands.
$(VERBOSE).SILENT:


# A target that is always out of date.
cmake_force:

.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /opt/local/bin/cmake

# The command to remove a file.
RM = /opt/local/bin/cmake -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /Users/johnson_marcus/Downloads/gr-my_module

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /Users/johnson_marcus/Downloads/gr-my_module/build

# Include any dependencies generated for this target.
include swig/CMakeFiles/_my_module_swig.dir/depend.make

# Include the progress variables for this target.
include swig/CMakeFiles/_my_module_swig.dir/progress.make

# Include the compile flags for this target's objects.
include swig/CMakeFiles/_my_module_swig.dir/flags.make

swig/my_module_swigPYTHON_wrap.cxx: swig/my_module_swig_swig_2d0df
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --blue --bold --progress-dir=/Users/johnson_marcus/Downloads/gr-my_module/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "dummy command to show my_module_swig_swig_2d0df dependency of /Users/johnson_marcus/Downloads/gr-my_module/build/swig/my_module_swigPYTHON_wrap.cxx"
	cd /Users/johnson_marcus/Downloads/gr-my_module/build/swig && /opt/local/bin/cmake -E touch_nocreate /Users/johnson_marcus/Downloads/gr-my_module/build/swig/my_module_swigPYTHON_wrap.cxx

swig/my_module_swig.py: swig/my_module_swig_swig_2d0df
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --blue --bold --progress-dir=/Users/johnson_marcus/Downloads/gr-my_module/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "dummy command to show my_module_swig_swig_2d0df dependency of /Users/johnson_marcus/Downloads/gr-my_module/build/swig/my_module_swig.py"
	cd /Users/johnson_marcus/Downloads/gr-my_module/build/swig && /opt/local/bin/cmake -E touch_nocreate /Users/johnson_marcus/Downloads/gr-my_module/build/swig/my_module_swig.py

swig/CMakeFiles/_my_module_swig.dir/my_module_swigPYTHON_wrap.cxx.o: swig/CMakeFiles/_my_module_swig.dir/flags.make
swig/CMakeFiles/_my_module_swig.dir/my_module_swigPYTHON_wrap.cxx.o: swig/my_module_swigPYTHON_wrap.cxx
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/Users/johnson_marcus/Downloads/gr-my_module/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_3) "Building CXX object swig/CMakeFiles/_my_module_swig.dir/my_module_swigPYTHON_wrap.cxx.o"
	cd /Users/johnson_marcus/Downloads/gr-my_module/build/swig && /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/_my_module_swig.dir/my_module_swigPYTHON_wrap.cxx.o -c /Users/johnson_marcus/Downloads/gr-my_module/build/swig/my_module_swigPYTHON_wrap.cxx

swig/CMakeFiles/_my_module_swig.dir/my_module_swigPYTHON_wrap.cxx.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/_my_module_swig.dir/my_module_swigPYTHON_wrap.cxx.i"
	cd /Users/johnson_marcus/Downloads/gr-my_module/build/swig && /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /Users/johnson_marcus/Downloads/gr-my_module/build/swig/my_module_swigPYTHON_wrap.cxx > CMakeFiles/_my_module_swig.dir/my_module_swigPYTHON_wrap.cxx.i

swig/CMakeFiles/_my_module_swig.dir/my_module_swigPYTHON_wrap.cxx.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/_my_module_swig.dir/my_module_swigPYTHON_wrap.cxx.s"
	cd /Users/johnson_marcus/Downloads/gr-my_module/build/swig && /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /Users/johnson_marcus/Downloads/gr-my_module/build/swig/my_module_swigPYTHON_wrap.cxx -o CMakeFiles/_my_module_swig.dir/my_module_swigPYTHON_wrap.cxx.s

# Object files for target _my_module_swig
_my_module_swig_OBJECTS = \
"CMakeFiles/_my_module_swig.dir/my_module_swigPYTHON_wrap.cxx.o"

# External object files for target _my_module_swig
_my_module_swig_EXTERNAL_OBJECTS =

swig/_my_module_swig.so: swig/CMakeFiles/_my_module_swig.dir/my_module_swigPYTHON_wrap.cxx.o
swig/_my_module_swig.so: swig/CMakeFiles/_my_module_swig.dir/build.make
swig/_my_module_swig.so: lib/libgnuradio-my_module.1.0.0git.dylib
swig/_my_module_swig.so: /usr/local/lib/libboost_filesystem-mt.dylib
swig/_my_module_swig.so: /usr/local/lib/libboost_system-mt.dylib
swig/_my_module_swig.so: /opt/local/lib/libgnuradio-runtime.dylib
swig/_my_module_swig.so: /opt/local/lib/libgnuradio-pmt.dylib
swig/_my_module_swig.so: /opt/local/lib/liblog4cpp.dylib
swig/_my_module_swig.so: swig/CMakeFiles/_my_module_swig.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/Users/johnson_marcus/Downloads/gr-my_module/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_4) "Linking CXX shared module _my_module_swig.so"
	cd /Users/johnson_marcus/Downloads/gr-my_module/build/swig && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/_my_module_swig.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
swig/CMakeFiles/_my_module_swig.dir/build: swig/_my_module_swig.so

.PHONY : swig/CMakeFiles/_my_module_swig.dir/build

swig/CMakeFiles/_my_module_swig.dir/clean:
	cd /Users/johnson_marcus/Downloads/gr-my_module/build/swig && $(CMAKE_COMMAND) -P CMakeFiles/_my_module_swig.dir/cmake_clean.cmake
.PHONY : swig/CMakeFiles/_my_module_swig.dir/clean

swig/CMakeFiles/_my_module_swig.dir/depend: swig/my_module_swigPYTHON_wrap.cxx
swig/CMakeFiles/_my_module_swig.dir/depend: swig/my_module_swig.py
	cd /Users/johnson_marcus/Downloads/gr-my_module/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /Users/johnson_marcus/Downloads/gr-my_module /Users/johnson_marcus/Downloads/gr-my_module/swig /Users/johnson_marcus/Downloads/gr-my_module/build /Users/johnson_marcus/Downloads/gr-my_module/build/swig /Users/johnson_marcus/Downloads/gr-my_module/build/swig/CMakeFiles/_my_module_swig.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : swig/CMakeFiles/_my_module_swig.dir/depend

