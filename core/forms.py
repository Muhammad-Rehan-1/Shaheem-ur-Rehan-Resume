from django import forms

INPUT_CLASSES = (
    "w-full rounded-xl px-4 py-3 transition border "
    "bg-[var(--surface-muted)] border-[var(--border)] text-[color:var(--text)] "
    "placeholder:text-[color:var(--text-muted)] "
    "focus:outline-none focus:border-[var(--accent)] focus:ring-1 focus:ring-[var(--accent)]"
)


class ContactForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={"class": INPUT_CLASSES, "placeholder": "Your Name"}),
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={"class": INPUT_CLASSES, "placeholder": "your.email@example.com"}),
    )
    subject = forms.CharField(
        max_length=150,
        widget=forms.TextInput(attrs={"class": INPUT_CLASSES, "placeholder": "Inquiry regarding..."}),
    )
    message = forms.CharField(
        widget=forms.Textarea(attrs={"class": INPUT_CLASSES + " h-32", "placeholder": "Write your message here..."}),
    )