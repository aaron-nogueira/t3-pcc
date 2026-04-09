{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "16e8c276",
   "metadata": {},
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "6cddc235",
   "metadata": {},
   "outputs": [],
   "source": [
    "from digraph import Digraph\n",
    "from DirectedEulerianCycle import DirectedEulerianCycle\n",
    "import os\n",
    "\n",
    "def main():\n",
    "    \n",
    "    path = os.path.join(os.path.dirname(__file__), '..', 'dados', 'entrada_eulerizada.txt')\n",
    "    \n",
    "    if not os.path.exists(path):\n",
    "        print(f\"Arquivo não encontrado: {path}\")\n",
    "        return\n",
    "\n",
    "    with open(path, 'r') as f:\n",
    "        V = int(f.readline())\n",
    "        E = int(f.readline())\n",
    "        G = Digraph(V)\n",
    "        \n",
    "        for line in f:\n",
    "            parts = line.split()\n",
    "            if len(parts) < 3: continue\n",
    "            v, w, weight = int(parts[0]), int(parts[1]), float(parts[2])\n",
    "            G.add_edge(v, w, weight)\n",
    "\n",
    "    print(\"--- Verificação de Graus ---\")\n",
    "    for v in range(G.V()):\n",
    "        print(f\"Vértice {v}: Entrada={G.indegree(v)}, Saída={G.outdegree(v)}\")\n",
    "\n",
    "    euler = DirectedEulerianCycle(G)\n",
    "\n",
    "    if euler.has_cycle():\n",
    "        path_vertices = euler.cycle()\n",
    "        print(\"\\n--- Circuito Euleriano ---\")\n",
    "        print(\" -> \".join(map(str, path_vertices)))\n",
    "\n",
    "        \n",
    "        total_cost = 0\n",
    "        temp_adj = [G.adj(v)[:] for v in range(G.V())] \n",
    "        \n",
    "        for i in range(len(path_vertices) - 1):\n",
    "            v_from = path_vertices[i]\n",
    "            v_to = path_vertices[i+1]\n",
    "            \n",
    "            for edge in temp_adj[v_from]:\n",
    "                if edge.to_vertex() == v_to:\n",
    "                    total_cost += edge.weight()\n",
    "                    temp_adj[v_from].remove(edge)\n",
    "                    break\n",
    "        \n",
    "        print(f\"\\nCusto Total do Circuito: {total_cost}\")\n",
    "    else:\n",
    "        print(\"\\nO grafo não possui um circuito euleriano (está desbalanceado).\")\n",
    "\n",
    "if __name__ == \"__main__\":\n",
    "    main()"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.13.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
