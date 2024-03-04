user_tasks = input("Enter your tasks for today separated by a comma: \n").split(", ")
done_tasks = []
ongoing_tasks = []
for task in user_tasks:
  print(f"\n{task}\n")
  done = input(f"Did you finish {task} already? (yes/no): \n").lower()
  if done == "yes":
    print("Nice job")
    done_tasks.append(task)
  else:
    print("Try not to put it off")
    ongoing_tasks.append(task)
  print("\n________")
progress = input("Do you want to see your today's progress? (yes/no): \n").lower()
if progress == "yes":
  print("\n.           ****** Done Tasks ******")
  print(done_tasks)
  print("\n.           ****** Done Tasks ******")
  print(ongoing_tasks)
input("\nPress Enter to exit...")