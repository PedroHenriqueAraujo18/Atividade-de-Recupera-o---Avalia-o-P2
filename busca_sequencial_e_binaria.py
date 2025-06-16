import tkinter as tk
from tkinter import ttk
import time
import random
import matplotlib.pyplot as plt
import numpy as np

# Armazenamento dos dados de teste para os gráficos
test_sizes = []
linear_times = []
binary_times = []
linear_visits = []
binary_visits = []

def linear_search(data, target):
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
    _, vis_l_abs, t_l_abs = linear_search(dataset, target_absent)
    _, vis_b_abs, t_b_abs = binary_search(dataset, target_absent)
    output_box.insert(tk.END, f"Linear Search (O(n))  - Visitas: {vis_l_abs}, Tempo: {t_l_abs:.6f}s\n")
    output_box.insert(tk.END, f"Binary Search (O(log n)) - Visitas: {vis_b_abs}, Tempo: {t_b_abs:.6f}s\n\n")

    # Salvar resultados para os gráficos (pior caso linear e binário)
    test_sizes.append(size)
    linear_times.append(t_l_abs)
    binary_times.append(t_b_abs)
    linear_visits.append(vis_l_abs)
    binary_visits.append(vis_b_abs)

def run_custom():
    try:
        size = int(entry_custom_size.get())
        run_tests_with_size(size)
    except ValueError:
        output_box.insert(tk.END, "⚠️ Por favor, insira um número válido.\n")

def plot_graphs():
    if not test_sizes:
        output_box.insert(tk.END, "⚠️ Por favor, execute alguns testes antes de gerar os gráficos.\n")
        return

    sizes_np = np.array(test_sizes)

    # Gráfico 1: Tempo de execução
    plt.figure()
    plt.plot(sizes_np, linear_times, marker='o', label='Linear Search (O(n))')
    plt.plot(sizes_np, binary_times, marker='s', label='Binary Search (O(log n))')
    plt.xlabel('Tamanho da Entrada')
    plt.ylabel('Tempo (segundos)')
    plt.title('Tempo vs Tamanho da Entrada (Pior Caso)')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

    # Gráfico 2: Número de Visitas
    plt.figure()
    plt.plot(sizes_np, linear_visits, marker='o', label='Linear Search (O(n))')
    plt.plot(sizes_np, binary_visits, marker='s', label='Binary Search (O(log n))')
    plt.xlabel('Tamanho da Entrada')
    plt.ylabel('Número de Visitas')
    plt.title('Número de Visitas vs Tamanho da Entrada (Pior Caso)')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

def build_interface():
    global entry_custom_size, output_box

    root = tk.Tk()
    root.title("Comparação: Busca Linear vs Binária")

    frame = ttk.Frame(root, padding=20)
    frame.grid()

    ttk.Label(frame, text="Escolha um tamanho de lista:").grid(row=0, column=0, columnspan=4)

    # Botões pré-definidos
    ttk.Button(frame, text="1.000 elementos", command=lambda: run_tests_with_size(1000)).grid(row=1, column=0, pady=5)
    ttk.Button(frame, text="10.000 elementos", command=lambda: run_tests_with_size(10000)).grid(row=1, column=1, pady=5)
    ttk.Button(frame, text="100.000 elementos", command=lambda: run_tests_with_size(100000)).grid(row=1, column=2, pady=5)

    # Entrada personalizada
    ttk.Label(frame, text="Tamanho personalizado:").grid(row=2, column=0)
    entry_custom_size = ttk.Entry(frame, width=10)
    entry_custom_size.insert(0, "1000000")
    entry_custom_size.grid(row=2, column=1)
    ttk.Button(frame, text="Executar", command=run_custom).grid(row=2, column=2)

    # Botão para mostrar gráficos
    ttk.Button(frame, text="📈 Mostrar Gráficos", command=plot_graphs).grid(row=2, column=3, padx=5)

    # Área de resultados
    output_box = tk.Text(frame, width=85, height=25)
    output_box.grid(row=3, column=0, columnspan=4, pady=10)

    root.mainloop()

if __name__ == "__main__":
    build_interface()
