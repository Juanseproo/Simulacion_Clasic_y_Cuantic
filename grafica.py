import numpy as np
import matplotlib.pyplot as plt

def graficar_vector_estado(vector_estado, nombres_objetivos=None, guardar_imagen=False, nombre_imagen="vector_estado.png"):
    """
    Cree una función para graficar con un diagrama de barras que muestre las probabilidades de un vector de estados. La imagen se debe poder guardar en el computador con un formato de imagen.
    -vector_estado (np.ndarray): Vector de estado a graficar.
    -nombres_objetivos (list): Lista de nombres para etiquetar los objetivos en el eje x.
    -guardar_imagen (bool): Indica si se debe guardar la imagen en el computador.
    -nombre_imagen (str): Nombre del archivo de imagen a guardar.
    """
    objetivos = len(vector_estado)
    x = np.arange(objetivos)
    
    plt.figure(figsize=(8, 6))
    plt.bar(x, np.abs(vector_estado))
    
    if nombres_objetivos:
        plt.xticks(x, nombres_objetivos, rotation=45, fontsize=12)
    
    plt.ylabel('Amplitud de Probabilidad', fontsize=14)
    plt.title('Vector de Estado', fontsize=16)
    plt.tight_layout()
    
    if guardar_imagen:
        plt.savefig(nombre_imagen)
        print("Imagen guardada como: ", nombre_imagen)
    else:
        plt.show()

# Ejemplo
if __name__ == "__main__":
    estado_final = np.array([0.2, 0.5, 0.3])
    nombres_objetivos = ['Objetivo A', 'Objetivo B', 'Objetivo C']
    graficar_vector_estado(estado_final, nombres_objetivos, guardar_imagen=True)
