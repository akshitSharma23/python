{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 85,
   "id": "9b9f6442",
   "metadata": {},
   "outputs": [],
   "source": [
    "import datetime\n",
    "#import date\n",
    "class person():\n",
    "    def __init__(self,name,DD,MM,YY,adhar,address):\n",
    "        self.name=name\n",
    "        self.DD=DD\n",
    "        self.MM=MM\n",
    "        self.YY=YY\n",
    "        self.adhar=adhar\n",
    "        self.address=address\n",
    "    def age(self):\n",
    "        CD=datetime.datetime(2021,12,28)\n",
    "        ag=a.strftime(\"%Y\")\n",
    "        #pint(ag)\n",
    "        print(f\"current age is {self.YY-int(ag)}\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 86,
   "id": "c7027a81",
   "metadata": {},
   "outputs": [],
   "source": [
    "per=person(\"askhit\",12,9,2021,20210215215,\"delhi\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 87,
   "id": "bd8cd3d7",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "current age is 3\n"
     ]
    }
   ],
   "source": [
    "per.age()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 88,
   "id": "db89712a",
   "metadata": {},
   "outputs": [],
   "source": [
    "class student(person):\n",
    "    def __init__(self,name,DD,MM,YY,adhar,address,rollno,stdname,school,classname,subject,marks):\n",
    "        person.__init__(self,name,DD,MM,YY,adhar,address)\n",
    "        self.name=name\n",
    "        self.DD=DD\n",
    "        self.MM=MM\n",
    "        self.YY=YY\n",
    "        self.adhar=adhar\n",
    "        self.address=address\n",
    "        self.rollno=rollno\n",
    "        self.stdname=stdname\n",
    "        self.school=school\n",
    "        self.classname=classname\n",
    "        self.subject=subject\n",
    "        self.marks=marks\n",
    "    def per(self):\n",
    "        l=len(self.marks)\n",
    "        a=0\n",
    "        for i in self.marks:\n",
    "            a=a+i\n",
    "        print((a/l)*100)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 89,
   "id": "e49a4880",
   "metadata": {},
   "outputs": [
    {
     "ename": "TypeError",
     "evalue": "__init__() takes 7 positional arguments but 13 were given",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mTypeError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-89-dae516fecdd7>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[1;32m----> 1\u001b[1;33m \u001b[0mper\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0mperson\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m\"askhit\"\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;36m12\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;36m9\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;36m2021\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;36m20210215215\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;34m\"delhi\"\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;36m202101440\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;34m\"akshit\"\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;34m\"tiet\"\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;34m\"mca\"\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;33m[\u001b[0m\u001b[1;34m\"eng\"\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;34m\"hind\"\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;34m\"CG\"\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;34m\"OS\"\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;34m\"DS\"\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;34m\"DBMS\"\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;33m[\u001b[0m\u001b[1;36m20\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;36m20\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;36m20\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;36m20\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;36m20\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;36m20\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[1;31mTypeError\u001b[0m: __init__() takes 7 positional arguments but 13 were given"
     ]
    }
   ],
   "source": [
    "per=person(\"askhit\",12,9,2021,20210215215,\"delhi\",202101440,\"akshit\",\"tiet\",\"mca\",[\"eng\",\"hind\",\"CG\",\"OS\",\"DS\",\"DBMS\"],[20,20,20,20,20,20])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "0df69a0d",
   "metadata": {},
   "outputs": [],
   "source": []
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
   "version": "3.8.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
