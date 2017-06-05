# Log-Analysis

## Overview:
>In this project, we have to query a DB which could actually be a real world DB having information like HTTP codes and authors of articles. We have to Find out the top three popular posts, most popular authors and days with `>1%` errors

#### PreRequisites:
  *  [Python2](https://www.python.org/)
  *  [Vagrant](https://www.vagrantup.com/)
  *  [VirtualBox](https://www.virtualbox.org/)

### Views Created :

#### ArticleHits:
```
create view articleHits as select title,author,count(path) as hits from articles,log where slug=substr(path, 10) group by articles.title,articles.author order by hits desc;
```

### Running the script :

##### Firing up the VM :
* Run `vagrant up`
* Run `Vagrant ssh`

##### Running queries on DB :
* Change directory using `cd /vagrant`
* Run `python2 logparser.py`
