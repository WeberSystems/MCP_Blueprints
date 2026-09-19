import sys, unreal
sys.path.append(r'C:\Program Files\Epic Games\UE_5.8\Engine\Plugins\Experimental\Toolsets\EditorToolset\Content\Python')
from editor_toolset.toolsets.blueprint import BlueprintTools
bp=unreal.load_object(None,'/Game/Interactables/BP_InteractableCanister.BP_InteractableCanister')
g=unreal.BlueprintEditorLibrary.find_event_graph(bp)
nodes=BlueprintTools.find_nodes(g)
unreal.log_warning('GRAPH_NODES '+str(len(nodes)))
for n in nodes:
    unreal.log_warning('GRAPH_NODE '+str(BlueprintTools._get_node_info(n).type_id))
try:
    unreal.log_warning('GRAPH_DSL '+BlueprintTools.read_graph_dsl(g))
except Exception as e:
    unreal.log_warning('GRAPH_DSL_ERROR '+str(e))
