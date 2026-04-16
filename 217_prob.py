{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 25,
   "id": "7c3b0680-39be-41dc-9b07-262c3b9a7147",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{1, 2, 3, 4}\n",
      "False\n"
     ]
    }
   ],
   "source": [
    "#217\n",
    "nums=[1,2,3,4]\n",
    "h=set()\n",
    "for i in nums:\n",
    "    h.add(i)\n",
    "print(h)\n",
    "if len(h)==len(nums):\n",
    "    print(False)\n",
    "else:\n",
    "    print(True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "id": "f50a7ef3-b595-419a-affe-ce82582656b8",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'c', 'a'}   {'c', 'a'}\n",
      "True\n"
     ]
    }
   ],
   "source": [
    "#242\n",
    "s=\"aacc\"\n",
    "t=\"ccac\"\n",
    "s1=set()\n",
    "t1=set()\n",
    "if len(s)==len(t):\n",
    "    for i in range(len(s)):\n",
    "        s1.add(s[i])\n",
    "        t1.add(t[i])\n",
    "print(s1,\" \",t1)\n",
    "if s1==t1:\n",
    "    print(True)\n",
    "else:\n",
    "    print(False)"
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
   "version": "3.13.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
