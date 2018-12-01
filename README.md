# PT:IO

As we get into the future, parent-teacher connections and relations will become more and more important. So why are we still using out-dated and difficult to use software? Introducing PT:IO! An easily accessible PTI for both parents, teachers, and administrators alike!
Parents -- Parents will be able to select their students and from then access the meeting pages of the teachers.
Teachers -- Teachers would add these windows/time frames to the classes and therefore have meetings for that class and that time.
Admin -- Administrators would be able to delete already graduated students, time specific dates for PTIs, and manage information.

__Authors:__

* [Jonathan Sumabat](https://github.com/jsumabat)
* [Moses Xu](https://github.com/plasmatic1)
* [Aaron Zhou](https://github.com/zhoaa)
* [Allen Pei](https://github.com/peiallen)

## Installed Applications

You will need [django](https://www.djangoproject.com/). That's it!

## Installation Process

**General Installation**

1. Clone the repository
2. Make the migrations
3. Run the application

**Beginner-Friendly Installation**

1. Open up Command Prompt (or Bash)
Refrence https://www.djangoproject.com/download/ 
2. Run the command `py -m pip install django`
4. Go to your directory of choice (for storing the program) and run `Git Bash` in that directory
5. In Git Bash, run the command `git clone https://github.com/jsumabat/ptio.git`
6. Go into the directory that the `git clone` command created
7. Run the command `py manage.py makemigrations`
8. Run the command `py manage.py migrate`
9. You're done!

Now, to start the server all you have to do is run the command `py manage.py runserver` in the directory of the program.  If you want to look at what else you can do with the application, you can always run `py manage.py --help` to look at different commands and `py manage.py runserver --help` to look at the different ways you can use the `runserver` command.
