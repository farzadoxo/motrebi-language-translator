namespace MLT_windows_app;

public partial class Form1 : Form
{
    public Form1()
    {
        InitializeComponent();
        // controls and commands
        outputTextBox.KeyDown += outputTextBox_KeyDown;
        translateButton.Click += translateButton_Click;
    }

    private void outputTextBox_KeyDown(object sender , KeyEventArgs e)
    {
        e.SuppressKeyPress = true;
    }

    private void translateButton_Click(object sender , EventArgs e)
    {
        try
        {
            string text = inputTextBox.Text;
            string newWord;
            string[] resaultText;
            string[] words = text.Split(" ");
            foreach(string i in words)
                foreach(char firstLetter in i)
                    if(firstLetter != 'ا' || firstLetter != 'آ' || firstLetter != 'ع')
                    {
                        newWord = i.Replace(firstLetter,'ا');
                        String.Join(firstLetter,newWord);
                        String.Join('و',newWord);
                        MessageBox.Show(newWord);
                        newWord = "";
                    }
                    else
                    {
                        newWord = i.Replace(firstLetter,'ش');
                        String.Join(firstLetter,newWord);
                        String.Join('و',newWord);
                        MessageBox.Show(newWord);
                        newWord = "";
                    }
                                
                    

        }
        catch
        {
            MessageBox.Show("در ترجمه مشکلی پیش آمد.");
        }
        

    }
}
