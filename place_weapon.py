import unreal
bp=unreal.load_asset('/Game/Weapons/BP_Rifle_Interact')
actors=unreal.get_editor_subsystem(unreal.EditorActorSubsystem)
existing=[a for a in actors.get_all_level_actors() if a.get_class()==bp.generated_class()]
if existing:
    weapon=existing[0]
else:
    start=next(a for a in actors.get_all_level_actors() if isinstance(a,unreal.PlayerStart))
    position=start.get_actor_location()+start.get_actor_forward_vector()*130
    position.z=start.get_actor_location().z-90+8
    weapon=actors.spawn_actor_from_class(bp.generated_class(),position,unreal.Rotator())
    weapon.set_actor_label('Rifle Interact - E to pick up')
    unreal.get_editor_subsystem(unreal.LevelEditorSubsystem).save_current_level()
actors.set_selected_level_actors([weapon])
unreal.log_warning('WEAPON_PLACED '+str(weapon.get_actor_location()))
