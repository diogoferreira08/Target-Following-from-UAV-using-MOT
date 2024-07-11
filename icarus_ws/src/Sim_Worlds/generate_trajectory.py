import random
import math

def generate_trajectory(num_people):
    trajectory = []
    max_time = 120
    x_range = (-15, 15)
    y_range = (-15, 15)
    speed_range = (1, 2)

    for i in range(num_people):
        waypoints = []
        num_waypoints = random.randint(6, 10)  # Random number of waypoints per person

        # Generate the first waypoint
        x1_aux = random.uniform(x_range[0], x_range[1])
        y1_aux = random.uniform(y_range[0], y_range[1])
        x = "{:.2f}".format(x1_aux)
        y = "{:.2f}".format(y1_aux)
        pose = f"{x} {y} 0 0 0 0"  # Assuming other pose parameters are 0
        angle = random.uniform(0, 2*math.pi)  # Random angle
        angle_aux = "{:.2f}".format(angle)
        waypoint = f"\t\t<waypoint>\n\t\t\t<time>0</time>\n\t\t\t<pose>{pose} {angle_aux}</pose>\n\t\t</waypoint>"
        waypoints.append(waypoint)

        for j in range(1, num_waypoints):
            x_prev, y_prev = map(float, waypoints[-1][2].split("<pose>")[1].split("</pose>")[0].split()[:2])
            time_prev = float(waypoints[-1].split("<time>")[1].split("</time>")[0])

            # Random direction and time
            direction = random.uniform(0, 2*math.pi)
            #max_speed = min(speed_range[1], calculate_max_speed(x_prev, y_prev, x_range, y_range, max_time - time_prev))
            speed = random.uniform(speed_range[0], speed_range[1])
            time_increment = random.uniform(0, max_time / num_waypoints)

            # Calculate new x and y
            x_new = min(x_range[1], max(x_prev + speed * time_increment * math.cos(direction), x_range[0]))
            y_new = min(y_range[1], max(y_prev + speed * time_increment * math.sin(direction), y_range[0]))

            # If out of bounds, mirror the waypoint in the opposite direction
            if x_new == x_range[1]:
                x_new = min(x_range[1], max(x_prev - speed * time_increment * math.cos(direction), x_range[0]))
            elif x_new == x_range[1]:
                x_new = min(x_range[1], max(x_prev - speed * time_increment * math.cos(direction), x_range[0]))
            if y_new == y_range[0]:
               y_new = min(y_range[1], max(y_prev - speed * time_increment * math.sin(direction), y_range[0]))
            elif y_new == y_range[1]:
                y_new = min(y_range[1], max(y_prev - speed * time_increment * math.sin(direction), y_range[0]))

            # Calculate new time
            time_new = time_prev + time_increment

            x_aux = x_new
            y_aux = y_new
            x_new = "{:.2f}".format(x_new)
            y_new = "{:.2f}".format(y_new)
            direction = "{:.2f}".format(direction)  
            
            # Create waypoint
            pose_new = f"{x_new} {y_new} 0 0 0 0"  # Assuming other pose parameters are 0
            #angle_new = random.uniform(0, 360)  # Random angle
            waypoint_new = f"\t\t<waypoint>\n\t\t\t<time>{time_new}</time>\n\t\t\t<pose>{pose_new} {direction}</pose>\n\t\t</waypoint>"
            #waypoints.append(waypoint_new)
            waypoint_new = f"\t\t<waypoint>\n\t\t\t<time>{time_new+0.5}</time>\n\t\t\t<pose>{pose_new} {direction}</pose>\n\t\t</waypoint>"
            #waypoints.append(waypoint_new)
            waypoints.append((x_aux, y_aux, waypoint_new))
        
        distance = math.sqrt((x_aux - x1_aux)**2 + (y_aux - y1_aux)**2)
        time = time_new + distance / speed_range[1]    
        waypoints.append(f"\t\t<waypoint>\n\t\t\t<time>{time}</time>\n\t\t\t<pose>{pose} {direction}</pose>\n\t\t</waypoint>")
        #trajectory.append("\t<trajectory id='{i}' type='walk' tension='1'>\n{waypoints}\n\t</trajectory>".format(i=i, waypoints='\n'.join(waypoints)))



        x_first, y_first, _ = waypoints[0]
        x_last, y_last, _ = waypoints[-1]
        angle = math.atan2(x_last - x_first, y_last - y_first)
        angle = "{:.2f}".format(angle)
        for i in range(len(waypoints)):
            x, y, waypoint = waypoints[i]
            waypoint = waypoint.replace("</pose>", f" {angle}</pose>")
            waypoints[i] = (x, y, waypoint)
        trajectory.append("\t<trajectory id='{i}' type='walk' tension='1'>\n{waypoints}\n\t</trajectory>".format(i=i, waypoints='\n'.join([waypoint for (_, _, waypoint) in waypoints])))

    return trajectory

def calculate_max_speed(x, y, x_range, y_range, remaining_time):
    max_dist_x = min(abs(x_range[1] - x), abs(x - x_range[0]))
    max_dist_y = min(abs(y_range[1] - y), abs(y - y_range[0]))
    max_dist = min(max_dist_x, max_dist_y)
    return max_dist / remaining_time

def generate_world_file(trajectories):
    with open("EXP1.world", "w") as file:
        file.write("""\
<?xml version="1.0" ?>
<?xml-model href="http://sdformat.org/schemas/root.xsd" schematypens="http://www.w3.org/2001/XMLSchema"?>
<sdf version="1.5">
    <world name="default">
        <!-- Add your plugin and other elements here -->
            <plugin name="mrs_gazebo_static_transform_republisher_plugin" filename="libMRSGazeboStaticTransformRepublisher.so"/>

            <!-- coordinate system {-->
            <spherical_coordinates>
            <surface_model>EARTH_WGS84</surface_model>
            <latitude_deg>47.397743</latitude_deg>
            <longitude_deg>8.545594</longitude_deg>
            <elevation>0.0</elevation>
            <heading_deg>0</heading_deg>
            </spherical_coordinates>
            <!--}-->

            <!-- physics engine {-->
            <physics name="default_physics" default="0" type="ode">
            <gravity>0 0 -9.8066</gravity>
            <ode>
                <solver>
                <type>quick</type>
                <iters>10</iters>
                <sor>1.3</sor>
                <use_dynamic_moi_rescaling>0</use_dynamic_moi_rescaling>
                </solver>
                <constraints>
                <cfm>0</cfm>
                <erp>0.2</erp>
                <contact_max_correcting_vel>1000</contact_max_correcting_vel>
                <contact_surface_layer>0.001</contact_surface_layer>
                </constraints>
            </ode>
            <max_step_size>0.004</max_step_size>
            <real_time_factor>1</real_time_factor>
            <real_time_update_rate>250</real_time_update_rate>
            <magnetic_field>6.0e-06 2.3e-05 -4.2e-05</magnetic_field>
            </physics>
            <!--}-->

            <!-- setup shadows {-->
            <scene>
            <shadows>false</shadows>
            <sky>
                <clouds/>
            </sky>
            </scene>
            <!--}-->

            <!-- sun {-->

            <light name='sun' type='directional'>
            <pose frame=''>0 0 1000 0.4 0.2 0</pose>
            <diffuse>1 1 1 1</diffuse>
            <specular>0.6 0.6 0.6 1</specular>
            <direction>0.1 0.1 -0.9</direction>
            <attenuation>
                <range>20</range>
                <constant>0.5</constant>
                <linear>0.01</linear>
                <quadratic>0.001</quadratic>
            </attenuation>
            <cast_shadows>1</cast_shadows>
            </light>

            <!--}-->

            <!-- ground plane {-->
            <model name="ground_plane">
            <static>true</static>
            <link name="link">
                <collision name="collision">
                <pose>0 0 0 0 0 0</pose>
                <geometry>
                    <plane>
                    <normal>0 0 1</normal>
                    <size>250 250</size>
                    </plane>
                </geometry>
                <surface>
                    <friction>
                    <ode>
                        <mu>1</mu>
                        <mu2>1</mu2>
                    </ode>
                    </friction>
                </surface>
                </collision>
                <visual name="grass">
                <pose>0 0 0 0 0 0</pose>
                <cast_shadows>false</cast_shadows>
                <geometry>
                    <mesh>
                    <uri>file://grass_plane/meshes/grass_plane.dae</uri>
                    </mesh>
                </geometry>
                <!-- <material> -->
                <!--   <script> -->
                <!--     <uri>file://media/materials/scripts/Gazebo.material</uri> -->
                <!--     <name>Gazebo/Grass</name> -->
                <!--   </script> -->
                <!-- </material> -->
                </visual>
            </link>
            </model>
            <!--}-->
                """)
        i=0
        for trajectory in trajectories:
            i+=1
            file.write("""<actor name="actor_walking"""+str(i)+"""">
                    <skin>
                        <filename>https://fuel.gazebosim.org/1.0/Mingfei/models/actor/tip/files/meshes/walk.dae</filename>
                        <scale>1.0</scale>
                    </skin>
                    <animation name="walk">
                        <filename>https://fuel.gazebosim.org/1.0/Mingfei/models/actor/tip/files/meshes/walk.dae</filename>
                        <interpolate_x>true</interpolate_x>
                    </animation>
                    <script>
                        <loop>true</loop>
                        <delay_start>0.000000</delay_start>
                        <auto_start>true</auto_start>
                   """+trajectory + "\n")
            file.write("""</script>
                </actor>""")
            
        file.write("""
                       <!-- THE VOID (for spawning objects out of camera view) {-->
            <model name='the_void'>
            <static>1</static>
            <link name='link'>
                <pose frame=''>0 0 0.1 0 -0 0</pose>
                <visual name='the_void'>
                <pose frame=''>0 0 2 0 -0 0</pose>
                <geometry>
                    <sphere>
                    <radius>0.25</radius>
                    </sphere>
                </geometry>
                <material>
                    <script>
                    <uri>file://media/materials/scripts/Gazebo.material</uri>
                    <name>Gazebo/Black</name>
                    </script>
                </material>
                </visual>
                <self_collide>0</self_collide>
                <enable_wind>0</enable_wind>
                <kinematic>0</kinematic>
            </link>
            <pose frame=''>-1000 -1000 0 0 0 0</pose>
            </model>
            <!--}-->

            <!-- user camera {-->
            <gui>
            <camera name="camera">
                <pose>-60 -100 30 0 0.4 0.89</pose>
            </camera>
            </gui>
            <!--}-->

            <!-- GUI frame synchronization {-->
            <plugin name="mrs_gazebo_rviz_cam_synchronizer" filename="libMRSGazeboRvizCameraSynchronizer.so" >
            <target_frame_id>gazebo_user_camera</target_frame_id>
            <world_origin_frame_id>uav1/gps_origin</world_origin_frame_id>
            <frame_to_follow>uav1</frame_to_follow>
            </plugin>
            <!--}-->

        </world>
        </sdf>
        """)

if __name__ == "__main__":
    num_people = random.randint(3, 6)
    trajectories = generate_trajectory(num_people)
    generate_world_file(trajectories)
