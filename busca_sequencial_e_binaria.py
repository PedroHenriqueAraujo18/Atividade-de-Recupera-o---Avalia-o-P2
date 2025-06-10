import tkinter as tk
from tkinter import ttk
import time
import random

def linear_search(data, target):
    """Busca sequencial.

    Args:
        data (list): Lista ordenada.
        target (int): Elemento a ser buscado.

    Returns:
        tuple: Índice do elemento, visitas, tempo em segundos.
    """
    visits = 0
    start = time.perf_counter()
    for index, element in enumerate(data):
        visits += 1
        if element == target:
            elapsed = time.perf_counter() - start
            return index, visits, elapsed
    elapsed = time.perf_counter() - start
    return -1, visits, elapsed

def binary_search(data, target):
    """Busca binária.

    Args:
        data (list): Lista ordenada.
        target (int): Elemento a ser buscado.

    Returns:
        tuple: Índice do elemento, visitas, tempo em segundos.
    """
    visits = 0
    start = time.perf_counter()
    left, right = 0, len(data) - 1

    while left <= right:
        mid = (left + right) // 2
        visits += 1
        if data[mid] == target:
            elapsed = time.perf_counter() - start
            return mid, visits, elapsed
        elif data[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    elapsed = time.perf_counter() - start
    return -1, visits, elapsed

def run_tests_with_size(size):
    """Executa os testes para um determinado tamanho de entrada.

    Args:
        size (int): Tamanho da lista de dados.
    """
    dataset = list(range(size))
    target_existing = random.choice(dataset)
    target_absent = -1

    output_box.insert(tk.END, f"\n=== Tamanho da Lista: {size} ===\n")

    # Caso Médio
    output_box.insert(tk.END, "[🔸 Caso Médio - Alvo Presente]\n")
    _, vis_l, t_l = linear_search(dataset, target_existing)
    _, vis_b, t_b = binary_search(dataset, target_existing)
    output_box.insert(tk.END, f"Linear Search (O(n))  - Visitas: {vis_l}, Tempo: {t_l:.6f}s\n")
    output_box.insert(tk.END, f"Binary Search (O(log n)) - Visitas: {vis_b}, Tempo: {t_b:.6f}s\n")

    # Pior Caso
    output_box.insert(tk.END, "[🔻 Pior Caso - Alvo Ausente]\n")
    _, vis_l, t_l = linear_search(dataset, target_absent)
    _, vis_b, t_b = binary_search(dataset, target_absent)
    output_box.insert(tk.END, f"Linear Search (O(n))  - Visitas: {vis_l}, Tempo: {t_l:.6f}s\n")
    output_box.insert(tk.END, f"Binary Search (O(log n)) - Visitas: {vis_b}, Tempo: {t_b:.6f}s\n\n")

def run_custom():
    """Executa teste com valor personalizado inserido pelo usuário."""
    try:
        size = int(entry_custom_size.get())
        run_tests_with_size(size)
    except ValueError:
        output_box.insert(tk.END, "⚠️ Por favor, insira um número válido.\n")

def build_interface():
    """Cria e exibe a interface gráfica."""
    root = tk.Tk()
    root.title("Comparação: Busca Linear vs Binária")

    frame = ttk.Frame(root, padding=20)
    frame.grid()

    # Título
    ttk.Label(frame, text="Escolha um tamanho de lista:").grid(row=0, column=0, columnspan=3)

    # Botões fixos
    ttk.Button(frame, text="1.000 elementos", command=lambda: run_tests_with_size(1000)).grid(row=1, column=0, pady=5)
    ttk.Button(frame, text="10.000 elementos", command=lambda: run_tests_with_size(10000)).grid(row=1, column=1, pady=5)
    ttk.Button(frame, text="100.000 elementos", command=lambda: run_tests_with_size(100000)).grid(row=1, column=2, pady=5)

    # Entrada personalizada
    ttk.Label(frame, text="Tamanho personalizado:").grid(row=2, column=0)
    global entry_custom_size
    entry_custom_size = ttk.Entry(frame, width=10)
    entry_custom_size.insert(0, "1000000")
    entry_custom_size.grid(row=2, column=1)

    ttk.Button(frame, text="Executar", command=run_custom).grid(row=2, column=2)

    # Área de resultados
    global output_box
    output_box = tk.Text(frame, width=70, height=20)
    output_box.grid(row=3, column=0, columnspan=3, pady=10)

    root.mainloop()

if __name__ == "__main__":
    build_interface()
