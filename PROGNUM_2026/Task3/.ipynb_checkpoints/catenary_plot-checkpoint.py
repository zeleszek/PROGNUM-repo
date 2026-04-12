{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "dea7b739-f0fb-4359-9177-9d2f33a6a088",
   "metadata": {},
   "outputs": [],
   "source": [
    "import matplotlib.pyplot as plt\n",
    "from math import e\n",
    "import numpy as np\n",
    "\n",
    "print(f\"using Python lists:\")\n",
    "X = list(range(-5, 6))\n",
    "Y = []\n",
    "\n",
    "for x in X:\n",
    "    y = ( e**x + e**(-x) ) / 2\n",
    "    Y.append(y)\n",
    "\n",
    "plt.subplots()\n",
    "plt.scatter(X, Y)\n",
    "plt.xlabel('x')\n",
    "plt.ylabel('cosh(x)')\n",
    "plt.grid(True)\n",
    "plt.title('catenary')\n",
    "plt.show()\n",
    "\n",
    "print(f\"using Numpy:\")\n",
    "\n",
    "x = np.linspace(-5, 5, num = 1000)\n",
    "y = ( e**x + e**(-x) ) / 2\n",
    "plt.subplots()\n",
    "plt.scatter(x, y)\n",
    "plt.xlabel('x')\n",
    "plt.ylabel('cosh(x)')\n",
    "plt.grid(True)\n",
    "plt.title('catenary')\n",
    "plt.show()"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
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
