{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "2de6cd7e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "7\n",
      "10\n"
     ]
    }
   ],
   "source": [
    "class A:\n",
    "    def __init__(self):\n",
    "        \n",
    "        self.x=7\n",
    "    \n",
    "    def disp(self):\n",
    "        \n",
    "        print(self.x)\n",
    "\n",
    "class B(A):\n",
    "    \n",
    "    def __init__(self):\n",
    "        \n",
    "        self.y=10\n",
    "        \n",
    "    def disp(self):\n",
    "        \n",
    "        print(self.y)\n",
    "\n",
    "obj=A()\n",
    "obj2=B()\n",
    "\n",
    "obj.disp()\n",
    "obj2.disp()\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "668dc24a",
   "metadata": {},
   "outputs": [],
   "source": [
    "Q3 (b)\n",
    "Q4 (c)\n",
    "Q5 ()"
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
   "version": "3.9.12"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}

#to show I just edited a cloned repo
import tensorflow as tf