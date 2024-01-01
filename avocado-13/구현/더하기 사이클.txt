{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "de0c2cb8",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "55\n",
      "3\n"
     ]
    }
   ],
   "source": [
    "N = int(input())\n",
    "count = 0\n",
    "origin = N\n",
    "\n",
    "while 1:\n",
    "  a = N//10\n",
    "  b = N%10\n",
    "  new_number = a+b\n",
    "  N = (b*10) + (new_number %10)\n",
    "  count += 1\n",
    "  if origin == N:\n",
    "    break\n",
    " \n",
    "print(count)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "bf42d9ff",
   "metadata": {},
   "outputs": [],
   "source": []
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
   "version": "3.9.13"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
