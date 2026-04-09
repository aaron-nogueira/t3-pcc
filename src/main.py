from digraph import Digraph
from DirectedEulerianCycle import DirectedEulerianCycle
import os

def main():
    
    path = os.path.join(os.path.dirname(__file__), '..', 'dados', 'entrada_eulerizada.txt')
    
    if not os.path.exists(path):
        print(f"Arquivo não encontrado: {path}")
        return

    with open(path, 'r') as f:
        V = int(f.readline())
        E = int(f.readline())
        G = Digraph(V)
        
        for line in f:
            parts = line.split()
            if len(parts) < 3: continue
            v, w, weight = int(parts[0]), int(parts[1]), float(parts[2])
            G.add_edge(v, w, weight)

    print("--- Verificação de Graus ---")
    for v in range(G.V()):
        print(f"Vértice {v}: Entrada={G.indegree(v)}, Saída={G.outdegree(v)}")

    euler = DirectedEulerianCycle(G)

    if euler.has_cycle():
        path_vertices = euler.cycle()
        print("\n--- Circuito Euleriano ---")
        print(" -> ".join(map(str, path_vertices)))

        
        total_cost = 0
        temp_adj = [G.adj(v)[:] for v in range(G.V())] 
        
        for i in range(len(path_vertices) - 1):
            v_from = path_vertices[i]
            v_to = path_vertices[i+1]
            
            for edge in temp_adj[v_from]:
                if edge.to_vertex() == v_to:
                    total_cost += edge.weight()
                    temp_adj[v_from].remove(edge)
                    break
        
        print(f"\nCusto Total do Circuito: {total_cost}")
    else:
        print("\nO grafo não possui um circuito euleriano (está desbalanceado).")

if __name__ == "__main__":
    main()