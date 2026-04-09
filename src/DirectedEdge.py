{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "8a691b8f",
   "metadata": {},
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "1deac2fb",
   "metadata": {},
   "outputs": [],
   "source": [
    "class DirectedEdge:\n",
    "    def __init__(self, v, w, weight):\n",
    "        self._v = v\n",
    "        self._w = w\n",
    "        self._weight = weight\n",
    "\n",
    "    def from_vertex(self):\n",
    "        return self._v\n",
    "\n",
    "    def to_vertex(self):\n",
    "        return self._w\n",
    "\n",
    "    def weight(self):\n",
    "        return self._weight\n",
    "\n",
    "    def __str__(self):\n",
    "        return f\"{self._v}->{self._w} ({self._weight})\""
   ]
  }
 ],
 "metadata": {
  "language_info": {
   "name": "python"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
