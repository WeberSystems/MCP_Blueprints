import sys, unreal
sys.path.append(r'C:\Program Files\Epic Games\UE_5.8\Engine\Plugins\Experimental\Toolsets\EditorToolset\Content\Python')
from editor_toolset.toolsets.blueprint import BlueprintTools as B
bp=unreal.load_asset('/Game/ThirdPerson/Blueprints/BP_ThirdPersonCharacter')
g=unreal.BlueprintEditorLibrary.find_event_graph(bp)
types=B.find_node_types(g,'')
for term in ['Keyboard','LineTrace','Camera','SpawnActor','DistanceTo','LessEqual','GetForwardVector','Multiply','Add_Vector','Equal_Object','BreakHit','InputKey']:
    unreal.log_warning('WEAPON_TYPES '+term+' '+str([t for t in types if term.lower() in t.lower()]))
unreal.log_warning('WEAPON_GRAPH '+B.read_graph_dsl(g))
for a in unreal.get_editor_subsystem(unreal.EditorActorSubsystem).get_all_level_actors():
    if 'PlayerStart' in a.get_class().get_name(): unreal.log_warning('WEAPON_START '+str(a.get_actor_location()))
