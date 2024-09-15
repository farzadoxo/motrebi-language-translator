namespace MLT_windows_app;

partial class Form1
{
    /// <summary>
    ///  Required designer variable.
    /// </summary>
    private System.ComponentModel.IContainer components = null;

    /// <summary>
    ///  Clean up any resources being used.
    /// </summary>
    /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
    protected override void Dispose(bool disposing)
    {
        if (disposing && (components != null))
        {
            components.Dispose();
        }
        base.Dispose(disposing);
    }

    #region Windows Form Designer generated code

    /// <summary>
    ///  Required method for Designer support - do not modify
    ///  the contents of this method with the code editor.
    /// </summary>
    private void InitializeComponent()
    {
        this.components = new System.ComponentModel.Container();
        this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
        this.ClientSize = new System.Drawing.Size(580, 380);
        this.Text = "🎷MLT 0.1";
        this.FormBorderStyle = FormBorderStyle.Fixed3D;
        this.MaximizeBox = false;



        // Define components properties
        headerLabel = new Label
        {
            Text = "Welcome to MLT 👋",
            ForeColor = Color.Blue,
            Font = new Font("Calibri", 15),
            Location = new Point(2,2),
            Size = new Size(190,20)
        };
        
        inputLabel = new Label
        {
            Text = "Input :",
            ForeColor = Color.Black,
            Size = new Size(100,20),
            Location = new Point(2,30)
        };

        outputLabel = new Label
        {
            Text = "Output :",
            ForeColor = Color.Black,
            Size = new Size(100,20),
            Location = new Point(295,30)
        };

        inputTextBox = new TextBox
        {
            Multiline = true,
            Width = 280,
            Height = 250,
            Text = "متن خود را وارد کنید",
            Location = new Point(2,50)
        };

        outputTextBox = new TextBox
        {
            Multiline = true,
            Width = 280,
            Height = 250,
            Location = new Point(295,50)
        };

        translateButton = new Button
        {
            Text = "Translate",
            ForeColor = Color.White,
            BackColor = Color.Orange,
            Size = new Size(100,50),
            Location = new Point(100,310)
        };


        // Locating (place) objects and components
        this.Controls.Add(headerLabel);
        this.Controls.Add(inputLabel);
        this.Controls.Add(outputLabel);
        this.Controls.Add(inputTextBox);
        this.Controls.Add(outputTextBox);
        this.Controls.Add(translateButton);
    }


    // Define components
    // --------------------------
    private Label headerLabel;
    private Label inputLabel;
    private Label outputLabel;
    private TextBox inputTextBox;
    private TextBox outputTextBox;
    private Button translateButton;


    #endregion
}
