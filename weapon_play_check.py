import unreal
world=unreal.EditorLevelLibrary.get_game_world()
pc=unreal.GameplayStatics.get_player_controller(world,0)
player=unreal.GameplayStatics.get_player_character(world,0)
items=unreal.GameplayStatics.get_all_actors_of_class(world,unreal.load_asset('/Game/Weapons/BP_Rifle_Interact').generated_class())
held=unreal.GameplayStatics.get_all_actors_of_class(world,unreal.load_asset('/Game/Weapons/BP_Rifle_Connect').generated_class())
unreal.log_warning('WEAPON_PLAY ground='+str(len(items))+' held='+str(len(held)))
if held:
    for a in held:
        unreal.log_warning('WEAPON_ATTACHMENT '+str(a.get_attach_parent_actor()==player)+' '+str(a.get_attach_parent_socket_name()))
elif items:
    target=items[0].get_actor_location()
    cam=unreal.GameplayStatics.get_player_camera_manager(world,0)
    # Aim around the spring arm pivot; the camera lies behind this ray.
    arm=player.get_component_by_class(unreal.SpringArmComponent)
    pivot=arm.get_world_location()+arm.get_editor_property('target_offset')
    pc.set_control_rotation(unreal.MathLibrary.find_look_at_rotation(pivot,target))
    unreal.log_warning('WEAPON_AIM distance='+str(player.get_distance_to(items[0]))+' hand='+str(player.mesh.does_socket_exist('hand_r')))
import time
deadline=time.monotonic()+2
def report_weapon_test(dt):
    if time.monotonic()<deadline: return
    unreal.unregister_slate_post_tick_callback(weapon_test_handle)
    cm=unreal.GameplayStatics.get_player_camera_manager(world,0)
    start=cm.get_camera_location()
    end=start+unreal.MathLibrary.get_forward_vector(cm.get_camera_rotation())*2000
    hit=unreal.SystemLibrary.line_trace_single(world,start,end,unreal.TraceTypeQuery.TRACE_TYPE_QUERY1,False,[player],unreal.DrawDebugTrace.NONE,False)
    unreal.log_warning('WEAPON_TRACE '+str(hit))
    unreal.log_warning('WEAPON_COUNTS ground='+str(len(unreal.GameplayStatics.get_all_actors_of_class(world,unreal.load_asset('/Game/Weapons/BP_Rifle_Interact').generated_class())))+' held='+str(len(unreal.GameplayStatics.get_all_actors_of_class(world,unreal.load_asset('/Game/Weapons/BP_Rifle_Connect').generated_class()))))
weapon_test_handle=unreal.register_slate_post_tick_callback(report_weapon_test)
