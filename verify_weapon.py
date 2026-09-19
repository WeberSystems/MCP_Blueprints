import sys,unreal
sys.path.append(r'C:\Program Files\Epic Games\UE_5.8\Engine\Plugins\Experimental\Toolsets\EditorToolset\Content\Python')
from editor_toolset.toolsets.blueprint import BlueprintTools as B
from editor_toolset.toolsets.actor import ActorTools as A
for name in ['BP_Rifle_Interact','BP_Rifle_Connect']:
    bp=unreal.load_asset('/Game/Weapons/'+name)
    g=unreal.BlueprintEditorLibrary.find_event_graph(bp)
    ns=B.find_nodes(g)
    assert not any('Tick' in str(n.get_node_title()) for n in ns)
    B.compile_blueprint(bp,True)
    B.arrange_nodes(ns)
    for n in ns:
        info=B._get_node_info(n)
        unreal.log_warning('WEAPON_NODE '+info.type_id+' '+str([(p.name,p.value,len(p.connected_pins)) for p in list(info.input_pins)+list(info.output_pins)]))
    cdo=B.get_default_object(bp)
    unreal.log_warning('WEAPON_DEFAULT '+name+' '+str(cdo.get_editor_property('auto_receive_input')))
    for c in A.get_components(cdo,unreal.StaticMeshComponent.static_class()):
        unreal.log_warning('WEAPON_MESH '+str(c.get_editor_property('static_mesh'))+' '+str(c.get_editor_property('relative_scale3d'))+' '+str(c.get_collision_profile_name()))
    assert unreal.EditorAssetLibrary.save_loaded_asset(bp)
unreal.log_warning('WEAPON_VERIFIED')
