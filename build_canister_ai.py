import sys, unreal
sys.path.append(r'C:\Program Files\Epic Games\UE_5.8\Engine\Plugins\Experimental\Toolsets\EditorToolset\Content\Python')
from editor_toolset.toolsets.actor import ActorTools
from editor_toolset.toolsets.blueprint import BlueprintTools

PATH='/Game/Interactables'
NAME='BP_InteractableCanister'
bp=unreal.load_object(None, PATH+'/'+NAME+'.'+NAME)

graph=unreal.BlueprintEditorLibrary.find_event_graph(bp)
for old_node in list(BlueprintTools.find_nodes(graph)):
    BlueprintTools.delete_node(old_node)
def node(type_id, x, y):
    n=BlueprintTools.create_node(graph, type_id, unreal.IntPoint(x,y))
    if not n: raise RuntimeError('Could not create node '+type_id)
    return n
def pin(n, name):
    p=next((p for p in n.list_all_pins() if str(p.get_pin_name()).lower()==name.lower()), None)
    if not p: raise RuntimeError('Missing pin '+name+' on '+str(n)+'; available='+str([str(x.get_pin_name()) for x in n.list_all_pins()]))
    return p
event=BlueprintTools.add_event(bp, 'EventTick', unreal.IntPoint(-900,0))
pc=node('Game|GetPlayerController',-700,180)
is_e=node('Game|Player|IsInputKeyDown',-450,0)
branch=node('Utilities|FlowControl|Branch',-200,0)
get_character_id=next(x for x in BlueprintTools.find_node_types(graph,'GetPlayerCharacter') if x.endswith('GetPlayerCharacter'))
player=node(get_character_id,-700,420)
cast_type=next(x for x in BlueprintTools.find_node_types(graph,'CastToCharacter') if x.endswith('CastToCharacter'))
cast=node(cast_type,0,220)
mesh=node('Class|Character|GetMesh',220,220)
attach=node('Transformation|AttachActorToComponent',500,0)
pin(event,'then').try_create_connection(pin(branch,'execute'))
pin(pc,'returnvalue').try_create_connection(pin(is_e,'self'))
pin(is_e,'returnvalue').try_create_connection(pin(branch,'condition'))
pin(branch,'then').try_create_connection(pin(cast,'execute'))
pin(player,'returnvalue').try_create_connection(pin(cast,'object'))
pin(cast,'ascharacter').try_create_connection(pin(mesh,'self'))
pin(cast,'then').try_create_connection(pin(attach,'execute'))
pin(mesh,'mesh').try_create_connection(pin(attach,'parent'))
BlueprintTools.set_pin_value(BlueprintTools._pin_to_id(pin(is_e,'key')),'E')
BlueprintTools.set_pin_value(BlueprintTools._pin_to_id(pin(attach,'socketname')),'hand_r')
BlueprintTools.set_pin_value(BlueprintTools._pin_to_id(pin(attach,'locationrule')),'SnapToTarget')
BlueprintTools.set_pin_value(BlueprintTools._pin_to_id(pin(attach,'rotationrule')),'SnapToTarget')
BlueprintTools.set_pin_value(BlueprintTools._pin_to_id(pin(attach,'scalerule')),'KeepWorld')
bp.modify()
unreal.BlueprintEditorLibrary.compile_blueprint(bp)
unreal.EditorAssetLibrary.save_loaded_asset(bp)
unreal.EditorAssetLibrary.save_directory(PATH)
unreal.log('AI Blueprint saved: '+PATH+'/'+NAME)
