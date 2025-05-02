import csv
from django.core.management.base import BaseCommand
from apps.challenges.models import Challenge

class Command(BaseCommand):
    help = "Export challenge details to CSV"

    def handle(self, *args, **kwargs):
        filename = "challenges.csv"
        with open(filename, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            
            # Writing header row
            writer.writerow(["Challenge ID", "Title", "Description", "FAQs"])
            
            # Fetch challenges from DB
            challenges = Challenge.objects.all()
            for challenge in challenges:
                # Convert FAQ list to string (comma-separated)
                faq_str = "; ".join(challenge.faq) if challenge.faq else "No FAQs"
                
                writer.writerow([challenge.id, challenge.title, challenge.description, faq_str])
        
        self.stdout.write(self.style.SUCCESS(f"Successfully exported challenges to {filename}"))
