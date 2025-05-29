#define _USE_MATH_DEFINES
#pragma once
#include <iostream>
#include <fstream>
#include <iomanip>
#include <vector>
#include <cmath>
#include <functional>

double aa = 1.0, bb = 2.0, cc = 2.0, dd = 3.0, h, k;

double X(int i)
{
	return aa + h * i;
}
double Y(int i)
{
	return cc + k * i;
}


std::function<double(double, double)> F;
double mT(double x, double y) // GU
{
	return sin(M_PI * x * y);
}

double fT(double x, double y)  // test
{
	return  - M_PI * M_PI * (x * x + y * y) * sin(M_PI * x * y) ;
}
double fO(double x, double y) // main
{
	return - exp(- x * y * y);
}
double mu1(double y)
{
	return (y - 2) * (y - 3);
}
double mu2(double y)
{
	return y * (y - 2) * (y - 3);
}
double mu3(double x)
{
	return (x - 1) * (x - 2);
}
double mu4(double x)
{
	return x * (x - 1) * (x - 2);
}
double SCAL(double** a, double** b, int n, int m) {

	double sum = 0;

	for (int j = 1; j < m; j++)
		for (int i = 1; i < n; i++)
			sum += a[i][j] * b[i][j];
	return sum;
}

namespace MVR {

	using namespace System;
	using namespace System::ComponentModel;
	using namespace System::Collections;
	using namespace System::Windows::Forms;
	using namespace System::Data;
	using namespace System::Drawing;

	/// <summary>
	/// Сводка для MyForm
	/// </summary>
	public ref class MyForm : public System::Windows::Forms::Form
	{
	public:
		MyForm(void)
		{
			InitializeComponent();
			//
			//TODO: добавьте код конструктора
			//
		}

	protected:
		/// <summary>
		/// Освободить все используемые ресурсы.
		/// </summary>
		~MyForm()
		{
			if (components)
			{
				delete components;
			}
		}


	protected:

	private: System::Windows::Forms::GroupBox^ groupBox4;
	private: System::Windows::Forms::GroupBox^ groupBox5;
	private: System::Windows::Forms::Label^ label9;
	private: System::Windows::Forms::TextBox^ textBox6;
	private: System::Windows::Forms::TextBox^ textBox5;
	private: System::Windows::Forms::Label^ label8;
	private: System::Windows::Forms::Label^ label7;
	private: System::Windows::Forms::TextBox^ textBox8;
	private: System::Windows::Forms::TextBox^ textBox7;
	private: System::Windows::Forms::Label^ label10;
	private: System::Windows::Forms::Label^ label13;
	private: System::Windows::Forms::Label^ label11;
	private: System::Windows::Forms::Label^ label16;
	private: System::Windows::Forms::Label^ label15;
	private: System::Windows::Forms::DataGridView^ Tab1;
	private: System::Windows::Forms::DataGridViewTextBoxColumn^ Column4;
	private: System::Windows::Forms::DataGridViewTextBoxColumn^ Column3;
	private: System::Windows::Forms::GroupBox^ groupBox7;
	private: System::Windows::Forms::Button^ button1;
	private: System::Windows::Forms::RadioButton^ radioButton4;
	private: System::Windows::Forms::Label^ label1;
	private: System::Windows::Forms::RadioButton^ radioButton5;
	private: System::Windows::Forms::Label^ label17;
	private: System::Windows::Forms::TabControl^ tabControl1;
	private: System::Windows::Forms::TabPage^ tabPage1;
	private: System::Windows::Forms::TabPage^ tabPage2;
	private: System::Windows::Forms::DataGridView^ Tab2;

	private: System::Windows::Forms::DataGridViewTextBoxColumn^ dataGridViewTextBoxColumn1;
	private: System::Windows::Forms::DataGridViewTextBoxColumn^ dataGridViewTextBoxColumn2;
	private: System::Windows::Forms::TabPage^ tabPage3;
	private: System::Windows::Forms::DataGridView^ Tab3;

	private: System::Windows::Forms::DataGridViewTextBoxColumn^ dataGridViewTextBoxColumn3;
	private: System::Windows::Forms::DataGridViewTextBoxColumn^ dataGridViewTextBoxColumn4;


				 /// <summary>
				 /// Обязательная переменная конструктора.
				 /// </summary>
				 System::ComponentModel::Container^ components;

#pragma region Windows Form Designer generated code
				 /// <summary>
				 /// Требуемый метод для поддержки конструктора — не изменяйте 
				 /// содержимое этого метода с помощью редактора кода.
				 /// </summary>
				 void InitializeComponent(void)
				 {
					 System::ComponentModel::ComponentResourceManager^ resources = (gcnew System::ComponentModel::ComponentResourceManager(MyForm::typeid));
					 this->groupBox5 = (gcnew System::Windows::Forms::GroupBox());
					 this->textBox8 = (gcnew System::Windows::Forms::TextBox());
					 this->textBox7 = (gcnew System::Windows::Forms::TextBox());
					 this->label10 = (gcnew System::Windows::Forms::Label());
					 this->label9 = (gcnew System::Windows::Forms::Label());
					 this->textBox6 = (gcnew System::Windows::Forms::TextBox());
					 this->textBox5 = (gcnew System::Windows::Forms::TextBox());
					 this->label8 = (gcnew System::Windows::Forms::Label());
					 this->label7 = (gcnew System::Windows::Forms::Label());
					 this->Tab1 = (gcnew System::Windows::Forms::DataGridView());
					 this->Column4 = (gcnew System::Windows::Forms::DataGridViewTextBoxColumn());
					 this->Column3 = (gcnew System::Windows::Forms::DataGridViewTextBoxColumn());
					 this->groupBox4 = (gcnew System::Windows::Forms::GroupBox());
					 this->label17 = (gcnew System::Windows::Forms::Label());
					 this->label16 = (gcnew System::Windows::Forms::Label());
					 this->label15 = (gcnew System::Windows::Forms::Label());
					 this->label13 = (gcnew System::Windows::Forms::Label());
					 this->label11 = (gcnew System::Windows::Forms::Label());
					 this->groupBox7 = (gcnew System::Windows::Forms::GroupBox());
					 this->label1 = (gcnew System::Windows::Forms::Label());
					 this->button1 = (gcnew System::Windows::Forms::Button());
					 this->radioButton4 = (gcnew System::Windows::Forms::RadioButton());
					 this->radioButton5 = (gcnew System::Windows::Forms::RadioButton());
					 this->tabControl1 = (gcnew System::Windows::Forms::TabControl());
					 this->tabPage1 = (gcnew System::Windows::Forms::TabPage());
					 this->tabPage2 = (gcnew System::Windows::Forms::TabPage());
					 this->Tab2 = (gcnew System::Windows::Forms::DataGridView());
					 this->dataGridViewTextBoxColumn1 = (gcnew System::Windows::Forms::DataGridViewTextBoxColumn());
					 this->dataGridViewTextBoxColumn2 = (gcnew System::Windows::Forms::DataGridViewTextBoxColumn());
					 this->tabPage3 = (gcnew System::Windows::Forms::TabPage());
					 this->Tab3 = (gcnew System::Windows::Forms::DataGridView());
					 this->dataGridViewTextBoxColumn3 = (gcnew System::Windows::Forms::DataGridViewTextBoxColumn());
					 this->dataGridViewTextBoxColumn4 = (gcnew System::Windows::Forms::DataGridViewTextBoxColumn());
					 this->groupBox5->SuspendLayout();
					 (cli::safe_cast<System::ComponentModel::ISupportInitialize^>(this->Tab1))->BeginInit();
					 this->groupBox4->SuspendLayout();
					 this->groupBox7->SuspendLayout();
					 this->tabControl1->SuspendLayout();
					 this->tabPage1->SuspendLayout();
					 this->tabPage2->SuspendLayout();
					 (cli::safe_cast<System::ComponentModel::ISupportInitialize^>(this->Tab2))->BeginInit();
					 this->tabPage3->SuspendLayout();
					 (cli::safe_cast<System::ComponentModel::ISupportInitialize^>(this->Tab3))->BeginInit();
					 this->SuspendLayout();
					 // 
					 // groupBox5
					 // 
					 this->groupBox5->Controls->Add(this->textBox8);
					 this->groupBox5->Controls->Add(this->textBox7);
					 this->groupBox5->Controls->Add(this->label10);
					 this->groupBox5->Controls->Add(this->label9);
					 this->groupBox5->Controls->Add(this->textBox6);
					 this->groupBox5->Controls->Add(this->textBox5);
					 this->groupBox5->Controls->Add(this->label8);
					 this->groupBox5->Controls->Add(this->label7);
					 this->groupBox5->Font = (gcnew System::Drawing::Font(L"Microsoft Sans Serif", 14));
					 this->groupBox5->Location = System::Drawing::Point(15, 318);
					 this->groupBox5->Margin = System::Windows::Forms::Padding(4);
					 this->groupBox5->Name = L"groupBox5";
					 this->groupBox5->Padding = System::Windows::Forms::Padding(4);
					 this->groupBox5->Size = System::Drawing::Size(338, 223);
					 this->groupBox5->TabIndex = 2;
					 this->groupBox5->TabStop = false;
					 this->groupBox5->Text = L"Параметры";
					 // 
					 // textBox8
					 // 
					 this->textBox8->Location = System::Drawing::Point(84, 170);
					 this->textBox8->Margin = System::Windows::Forms::Padding(4);
					 this->textBox8->Name = L"textBox8";
					 this->textBox8->Size = System::Drawing::Size(118, 34);
					 this->textBox8->TabIndex = 11;
					 this->textBox8->Text = L"0,0000005";
					 // 
					 // textBox7
					 // 
					 this->textBox7->Location = System::Drawing::Point(98, 127);
					 this->textBox7->Margin = System::Windows::Forms::Padding(4);
					 this->textBox7->Name = L"textBox7";
					 this->textBox7->Size = System::Drawing::Size(104, 34);
					 this->textBox7->TabIndex = 10;
					 this->textBox7->Text = L"5500";
					 // 
					 // label10
					 // 
					 this->label10->AutoSize = true;
					 this->label10->Location = System::Drawing::Point(6, 173);
					 this->label10->Margin = System::Windows::Forms::Padding(4, 0, 4, 0);
					 this->label10->Name = L"label10";
					 this->label10->Size = System::Drawing::Size(81, 29);
					 this->label10->TabIndex = 9;
					 this->label10->Text = L"Eps = ";
					 // 
					 // label9
					 // 
					 this->label9->AutoSize = true;
					 this->label9->Location = System::Drawing::Point(6, 130);
					 this->label9->Margin = System::Windows::Forms::Padding(4, 0, 4, 0);
					 this->label9->Name = L"label9";
					 this->label9->Size = System::Drawing::Size(101, 29);
					 this->label9->TabIndex = 8;
					 this->label9->Text = L"Nmax = ";
					 // 
					 // textBox6
					 // 
					 this->textBox6->Location = System::Drawing::Point(81, 85);
					 this->textBox6->Margin = System::Windows::Forms::Padding(4);
					 this->textBox6->Name = L"textBox6";
					 this->textBox6->Size = System::Drawing::Size(121, 34);
					 this->textBox6->TabIndex = 7;
					 this->textBox6->Text = L"4";
					 // 
					 // textBox5
					 // 
					 this->textBox5->Location = System::Drawing::Point(81, 41);
					 this->textBox5->Margin = System::Windows::Forms::Padding(4);
					 this->textBox5->Name = L"textBox5";
					 this->textBox5->Size = System::Drawing::Size(121, 34);
					 this->textBox5->TabIndex = 6;
					 this->textBox5->Text = L"4";
					 // 
					 // label8
					 // 
					 this->label8->AutoSize = true;
					 this->label8->Location = System::Drawing::Point(13, 85);
					 this->label8->Margin = System::Windows::Forms::Padding(4, 0, 4, 0);
					 this->label8->Name = L"label8";
					 this->label8->Size = System::Drawing::Size(59, 29);
					 this->label8->TabIndex = 5;
					 this->label8->Text = L"m = ";
					 // 
					 // label7
					 // 
					 this->label7->AutoSize = true;
					 this->label7->Location = System::Drawing::Point(13, 44);
					 this->label7->Margin = System::Windows::Forms::Padding(4, 0, 4, 0);
					 this->label7->Name = L"label7";
					 this->label7->Size = System::Drawing::Size(52, 29);
					 this->label7->TabIndex = 4;
					 this->label7->Text = L"n = ";
					 // 
					 // Tab1
					 // 
					 this->Tab1->Anchor = static_cast<System::Windows::Forms::AnchorStyles>((((System::Windows::Forms::AnchorStyles::Top | System::Windows::Forms::AnchorStyles::Bottom)
						 | System::Windows::Forms::AnchorStyles::Left)
						 | System::Windows::Forms::AnchorStyles::Right));
					 this->Tab1->BackgroundColor = System::Drawing::SystemColors::GradientActiveCaption;
					 this->Tab1->ColumnHeadersHeightSizeMode = System::Windows::Forms::DataGridViewColumnHeadersHeightSizeMode::AutoSize;
					 this->Tab1->Columns->AddRange(gcnew cli::array< System::Windows::Forms::DataGridViewColumn^  >(2) { this->Column4, this->Column3 });
					 this->Tab1->Location = System::Drawing::Point(7, 6);
					 this->Tab1->Margin = System::Windows::Forms::Padding(4);
					 this->Tab1->Name = L"Tab1";
					 this->Tab1->RowHeadersWidth = 62;
					 this->Tab1->Size = System::Drawing::Size(890, 223);
					 this->Tab1->TabIndex = 14;
					 // 
					 // Column4
					 // 
					 this->Column4->HeaderText = L"";
					 this->Column4->MinimumWidth = 8;
					 this->Column4->Name = L"Column4";
					 this->Column4->ReadOnly = true;
					 this->Column4->Width = 150;
					 // 
					 // Column3
					 // 
					 this->Column3->HeaderText = L"i";
					 this->Column3->MinimumWidth = 8;
					 this->Column3->Name = L"Column3";
					 this->Column3->ReadOnly = true;
					 this->Column3->Width = 150;
					 // 
					 // groupBox4
					 // 
					 this->groupBox4->Controls->Add(this->label17);
					 this->groupBox4->Controls->Add(this->label16);
					 this->groupBox4->Controls->Add(this->label15);
					 this->groupBox4->Controls->Add(this->label13);
					 this->groupBox4->Controls->Add(this->label11);
					 this->groupBox4->Font = (gcnew System::Drawing::Font(L"Microsoft Sans Serif", 12));
					 this->groupBox4->Location = System::Drawing::Point(444, 8);
					 this->groupBox4->Margin = System::Windows::Forms::Padding(4);
					 this->groupBox4->Name = L"groupBox4";
					 this->groupBox4->Padding = System::Windows::Forms::Padding(4);
					 this->groupBox4->Size = System::Drawing::Size(1228, 353);
					 this->groupBox4->TabIndex = 1;
					 this->groupBox4->TabStop = false;
					 this->groupBox4->Text = L"Справка";
					 // 
					 // label17
					 // 
					 this->label17->AutoSize = true;
					 this->label17->Location = System::Drawing::Point(891, 51);
					 this->label17->Margin = System::Windows::Forms::Padding(4, 0, 4, 0);
					 this->label17->Name = L"label17";
					 this->label17->Size = System::Drawing::Size(19, 25);
					 this->label17->TabIndex = 6;
					 this->label17->Text = L"-";
					 // 
					 // label16
					 // 
					 this->label16->AutoSize = true;
					 this->label16->Location = System::Drawing::Point(13, 186);
					 this->label16->Margin = System::Windows::Forms::Padding(4, 0, 4, 0);
					 this->label16->Name = L"label16";
					 this->label16->Size = System::Drawing::Size(0, 25);
					 this->label16->TabIndex = 5;
					 // 
					 // label15
					 // 
					 this->label15->AutoSize = true;
					 this->label15->Location = System::Drawing::Point(13, 158);
					 this->label15->Margin = System::Windows::Forms::Padding(4, 0, 4, 0);
					 this->label15->Name = L"label15";
					 this->label15->Size = System::Drawing::Size(0, 25);
					 this->label15->TabIndex = 4;
					 // 
					 // label13
					 // 
					 this->label13->AutoSize = true;
					 this->label13->Location = System::Drawing::Point(13, 91);
					 this->label13->Margin = System::Windows::Forms::Padding(4, 0, 4, 0);
					 this->label13->Name = L"label13";
					 this->label13->Size = System::Drawing::Size(0, 25);
					 this->label13->TabIndex = 2;
					 // 
					 // label11
					 // 
					 this->label11->AutoSize = true;
					 this->label11->Font = (gcnew System::Drawing::Font(L"Microsoft Sans Serif", 12));
					 this->label11->Location = System::Drawing::Point(21, 51);
					 this->label11->Margin = System::Windows::Forms::Padding(4, 0, 4, 0);
					 this->label11->Name = L"label11";
					 this->label11->Size = System::Drawing::Size(649, 225);
					 this->label11->TabIndex = 0;
					 this->label11->Text = resources->GetString(L"label11.Text");
					 // 
					 // groupBox7
					 // 
					 this->groupBox7->Controls->Add(this->label1);
					 this->groupBox7->Font = (gcnew System::Drawing::Font(L"Microsoft Sans Serif", 14));
					 this->groupBox7->Location = System::Drawing::Point(15, 63);
					 this->groupBox7->Margin = System::Windows::Forms::Padding(3, 2, 3, 2);
					 this->groupBox7->Name = L"groupBox7";
					 this->groupBox7->Padding = System::Windows::Forms::Padding(3, 2, 3, 2);
					 this->groupBox7->Size = System::Drawing::Size(422, 202);
					 this->groupBox7->TabIndex = 14;
					 this->groupBox7->TabStop = false;
					 this->groupBox7->Text = L"Описание задачи";
					 // 
					 // label1
					 // 
					 this->label1->AutoSize = true;
					 this->label1->Location = System::Drawing::Point(13, 27);
					 this->label1->Name = L"label1";
					 this->label1->Size = System::Drawing::Size(298, 145);
					 this->label1->TabIndex = 1;
					 this->label1->Text = L"u* = sin(πxy); x-[1,2], y-[2,3]\r\nu(1, y) = (y-2)(y-3),\r\nu(2, y) = y(y-2)(y-3), \r\n"
						 L"u(x, 2) = (x-1)(x-2),\r\nu(x,3) = x(x-1)(x-2)";
					 // 
					 // button1
					 // 
					 this->button1->Font = (gcnew System::Drawing::Font(L"Microsoft Sans Serif", 12));
					 this->button1->Location = System::Drawing::Point(290, 279);
					 this->button1->Margin = System::Windows::Forms::Padding(3, 2, 3, 2);
					 this->button1->Name = L"button1";
					 this->button1->Size = System::Drawing::Size(125, 33);
					 this->button1->TabIndex = 0;
					 this->button1->Text = L"Рассчет";
					 this->button1->UseVisualStyleBackColor = true;
					 this->button1->Click += gcnew System::EventHandler(this, &MyForm::button1_Click_1);
					 // 
					 // radioButton4
					 // 
					 this->radioButton4->AutoSize = true;
					 this->radioButton4->Checked = true;
					 this->radioButton4->Font = (gcnew System::Drawing::Font(L"Microsoft Sans Serif", 12));
					 this->radioButton4->Location = System::Drawing::Point(28, 10);
					 this->radioButton4->Margin = System::Windows::Forms::Padding(3, 2, 3, 2);
					 this->radioButton4->Name = L"radioButton4";
					 this->radioButton4->Size = System::Drawing::Size(189, 29);
					 this->radioButton4->TabIndex = 1;
					 this->radioButton4->TabStop = true;
					 this->radioButton4->Text = L"Тестовая задача";
					 this->radioButton4->UseVisualStyleBackColor = true;
					 this->radioButton4->CheckedChanged += gcnew System::EventHandler(this, &MyForm::radioButton4_CheckedChanged);
					 // 
					 // radioButton5
					 // 
					 this->radioButton5->AutoSize = true;
					 this->radioButton5->Font = (gcnew System::Drawing::Font(L"Microsoft Sans Serif", 12));
					 this->radioButton5->Location = System::Drawing::Point(28, 34);
					 this->radioButton5->Margin = System::Windows::Forms::Padding(3, 2, 3, 2);
					 this->radioButton5->Name = L"radioButton5";
					 this->radioButton5->Size = System::Drawing::Size(191, 29);
					 this->radioButton5->TabIndex = 15;
					 this->radioButton5->Text = L"Основная задача";
					 this->radioButton5->UseVisualStyleBackColor = true;
					 this->radioButton5->CheckedChanged += gcnew System::EventHandler(this, &MyForm::radioButton5_CheckedChanged);
					 // 
					 // tabControl1
					 // 
					 this->tabControl1->Anchor = static_cast<System::Windows::Forms::AnchorStyles>((((System::Windows::Forms::AnchorStyles::Top | System::Windows::Forms::AnchorStyles::Bottom)
						 | System::Windows::Forms::AnchorStyles::Left)
						 | System::Windows::Forms::AnchorStyles::Right));
					 this->tabControl1->Controls->Add(this->tabPage1);
					 this->tabControl1->Controls->Add(this->tabPage2);
					 this->tabControl1->Controls->Add(this->tabPage3);
					 this->tabControl1->Font = (gcnew System::Drawing::Font(L"Microsoft Sans Serif", 12));
					 this->tabControl1->Location = System::Drawing::Point(444, 367);
					 this->tabControl1->Margin = System::Windows::Forms::Padding(3, 2, 3, 2);
					 this->tabControl1->Name = L"tabControl1";
					 this->tabControl1->SelectedIndex = 0;
					 this->tabControl1->Size = System::Drawing::Size(912, 273);
					 this->tabControl1->TabIndex = 16;
					 // 
					 // tabPage1
					 // 
					 this->tabPage1->Controls->Add(this->Tab1);
					 this->tabPage1->Location = System::Drawing::Point(4, 34);
					 this->tabPage1->Margin = System::Windows::Forms::Padding(3, 2, 3, 2);
					 this->tabPage1->Name = L"tabPage1";
					 this->tabPage1->Padding = System::Windows::Forms::Padding(3, 2, 3, 2);
					 this->tabPage1->Size = System::Drawing::Size(904, 235);
					 this->tabPage1->TabIndex = 0;
					 this->tabPage1->Text = L"V ( x , y )";
					 this->tabPage1->UseVisualStyleBackColor = true;
					 // 
					 // tabPage2
					 // 
					 this->tabPage2->Controls->Add(this->Tab2);
					 this->tabPage2->Location = System::Drawing::Point(4, 34);
					 this->tabPage2->Margin = System::Windows::Forms::Padding(3, 2, 3, 2);
					 this->tabPage2->Name = L"tabPage2";
					 this->tabPage2->Padding = System::Windows::Forms::Padding(3, 2, 3, 2);
					 this->tabPage2->Size = System::Drawing::Size(904, 235);
					 this->tabPage2->TabIndex = 1;
					 this->tabPage2->Text = L"U ( x , y )";
					 this->tabPage2->UseVisualStyleBackColor = true;
					 // 
					 // Tab2
					 // 
					 this->Tab2->Anchor = static_cast<System::Windows::Forms::AnchorStyles>((((System::Windows::Forms::AnchorStyles::Top | System::Windows::Forms::AnchorStyles::Bottom)
						 | System::Windows::Forms::AnchorStyles::Left)
						 | System::Windows::Forms::AnchorStyles::Right));
					 this->Tab2->BackgroundColor = System::Drawing::SystemColors::GradientActiveCaption;
					 this->Tab2->ColumnHeadersHeightSizeMode = System::Windows::Forms::DataGridViewColumnHeadersHeightSizeMode::AutoSize;
					 this->Tab2->Columns->AddRange(gcnew cli::array< System::Windows::Forms::DataGridViewColumn^  >(2) {
						 this->dataGridViewTextBoxColumn1,
							 this->dataGridViewTextBoxColumn2
					 });
					 this->Tab2->Location = System::Drawing::Point(4, 6);
					 this->Tab2->Margin = System::Windows::Forms::Padding(4);
					 this->Tab2->Name = L"Tab2";
					 this->Tab2->RowHeadersWidth = 62;
					 this->Tab2->Size = System::Drawing::Size(893, 223);
					 this->Tab2->TabIndex = 15;
					 // 
					 // dataGridViewTextBoxColumn1
					 // 
					 this->dataGridViewTextBoxColumn1->HeaderText = L"";
					 this->dataGridViewTextBoxColumn1->MinimumWidth = 8;
					 this->dataGridViewTextBoxColumn1->Name = L"dataGridViewTextBoxColumn1";
					 this->dataGridViewTextBoxColumn1->ReadOnly = true;
					 this->dataGridViewTextBoxColumn1->Width = 150;
					 // 
					 // dataGridViewTextBoxColumn2
					 // 
					 this->dataGridViewTextBoxColumn2->HeaderText = L"i";
					 this->dataGridViewTextBoxColumn2->MinimumWidth = 8;
					 this->dataGridViewTextBoxColumn2->Name = L"dataGridViewTextBoxColumn2";
					 this->dataGridViewTextBoxColumn2->ReadOnly = true;
					 this->dataGridViewTextBoxColumn2->Width = 150;
					 // 
					 // tabPage3
					 // 
					 this->tabPage3->Controls->Add(this->Tab3);
					 this->tabPage3->Location = System::Drawing::Point(4, 34);
					 this->tabPage3->Margin = System::Windows::Forms::Padding(3, 2, 3, 2);
					 this->tabPage3->Name = L"tabPage3";
					 this->tabPage3->Size = System::Drawing::Size(904, 235);
					 this->tabPage3->TabIndex = 2;
					 this->tabPage3->Text = L"| U ( x , y) - V ( x , y ) |";
					 this->tabPage3->UseVisualStyleBackColor = true;
					 // 
					 // Tab3
					 // 
					 this->Tab3->Anchor = static_cast<System::Windows::Forms::AnchorStyles>((((System::Windows::Forms::AnchorStyles::Top | System::Windows::Forms::AnchorStyles::Bottom)
						 | System::Windows::Forms::AnchorStyles::Left)
						 | System::Windows::Forms::AnchorStyles::Right));
					 this->Tab3->BackgroundColor = System::Drawing::SystemColors::GradientActiveCaption;
					 this->Tab3->ColumnHeadersHeightSizeMode = System::Windows::Forms::DataGridViewColumnHeadersHeightSizeMode::AutoSize;
					 this->Tab3->Columns->AddRange(gcnew cli::array< System::Windows::Forms::DataGridViewColumn^  >(2) {
						 this->dataGridViewTextBoxColumn3,
							 this->dataGridViewTextBoxColumn4
					 });
					 this->Tab3->Location = System::Drawing::Point(6, 4);
					 this->Tab3->Margin = System::Windows::Forms::Padding(4);
					 this->Tab3->Name = L"Tab3";
					 this->Tab3->RowHeadersWidth = 62;
					 this->Tab3->Size = System::Drawing::Size(894, 227);
					 this->Tab3->TabIndex = 15;
					 // 
					 // dataGridViewTextBoxColumn3
					 // 
					 this->dataGridViewTextBoxColumn3->HeaderText = L"";
					 this->dataGridViewTextBoxColumn3->MinimumWidth = 8;
					 this->dataGridViewTextBoxColumn3->Name = L"dataGridViewTextBoxColumn3";
					 this->dataGridViewTextBoxColumn3->ReadOnly = true;
					 this->dataGridViewTextBoxColumn3->Width = 150;
					 // 
					 // dataGridViewTextBoxColumn4
					 // 
					 this->dataGridViewTextBoxColumn4->HeaderText = L"i";
					 this->dataGridViewTextBoxColumn4->MinimumWidth = 8;
					 this->dataGridViewTextBoxColumn4->Name = L"dataGridViewTextBoxColumn4";
					 this->dataGridViewTextBoxColumn4->ReadOnly = true;
					 this->dataGridViewTextBoxColumn4->Width = 150;
					 // 
					 // MyForm
					 // 
					 this->AutoScaleDimensions = System::Drawing::SizeF(8, 16);
					 this->AutoScaleMode = System::Windows::Forms::AutoScaleMode::Font;
					 this->ClientSize = System::Drawing::Size(1372, 651);
					 this->Controls->Add(this->tabControl1);
					 this->Controls->Add(this->button1);
					 this->Controls->Add(this->radioButton5);
					 this->Controls->Add(this->radioButton4);
					 this->Controls->Add(this->groupBox7);
					 this->Controls->Add(this->groupBox5);
					 this->Controls->Add(this->groupBox4);
					 this->Margin = System::Windows::Forms::Padding(4);
					 this->Name = L"MyForm";
					 this->Text = L"ММН, вариант 4, команда 4";
					 this->groupBox5->ResumeLayout(false);
					 this->groupBox5->PerformLayout();
					 (cli::safe_cast<System::ComponentModel::ISupportInitialize^>(this->Tab1))->EndInit();
					 this->groupBox4->ResumeLayout(false);
					 this->groupBox4->PerformLayout();
					 this->groupBox7->ResumeLayout(false);
					 this->groupBox7->PerformLayout();
					 this->tabControl1->ResumeLayout(false);
					 this->tabPage1->ResumeLayout(false);
					 this->tabPage2->ResumeLayout(false);
					 (cli::safe_cast<System::ComponentModel::ISupportInitialize^>(this->Tab2))->EndInit();
					 this->tabPage3->ResumeLayout(false);
					 (cli::safe_cast<System::ComponentModel::ISupportInitialize^>(this->Tab3))->EndInit();
					 this->ResumeLayout(false);
					 this->PerformLayout();

				 }
#pragma endregion
				 // =========  Functions =========


	private: System::Void radioButton4_CheckedChanged(System::Object^ sender, System::EventArgs^ e) {
		label1->Text = "u* = sin(pi*xy); x-[1,2], y-[2,3]\nu(1, y) = (y-2)(y-3)\nu(2, y) = y(y-2)(y-3)\nu(x, 2) = (x-1)(x-2)\nu(x,3) = x(x-1)(x-2)";
		label11->Text = "Количество итераций = \nПогрешность решения = \nНачальное приближения посчитано как \nНевязка СЛАУ на начальном приближении(евклидова норма) R(0) = \nСхема на сетке решена с невязкой(евклидова норма) R(p) = \nМаксимальная разность точного и численного решений | U - V |=\nx = \ny = ";
		tabPage2->Text = L"U ( x , y )";
		tabPage3->Text = L"| U ( x , y )-V ( x , y ) |";
	}
	private: System::Void radioButton5_CheckedChanged(System::Object^ sender, System::EventArgs^ e) {
		label1->Text = "u'xx + u'yy = sin(pi*xy)^2 при x-[1,2], y-[2,3]\nu(1, y) = (y-2)(y-3)\nu(2, y) = y(y-2)(y-3)\nu(x, 2) = (x-1)(x-2)\nu(x,3) = x(x-1)(x-2)";
		label11->Text = "Количество итераций = \nДостигнутая точность = \nНевязка СЛАУ на начальном приближении(евклидова норма) R(0) = \nСхема на сетке решена с невязкой(евклидова норма) R(p) = \nКоличество итераций при половинном шаге = \nДостигнутая точность = \nНевязка СЛАУ на начальном приближении(евклидова норма) R(0) = \nСхема на сетке с половинным шагом решена с невязкой(евклидова норма) R(p2) = \nМаксимальная разность двух решений | V2 - V | (точность решения) = \nв узле : \nx = \ny =";
		tabPage2->Text = L"V2 ( x , y )";
		tabPage3->Text = L"| V2 ( x , y )-V ( x , y ) |";
	}
	private: System::Void button1_Click_1(System::Object^ sender, System::EventArgs^ e) {

		int n, m, Nmax, p = 0, p2 = 0; //Текущее число итераций
		double h2, k2, Eps, A, MaxPogr = 0.0, Pogr, R0 = 0.0, xMax = 0.0, yMax = 0.0, Rn = 0.0, R02 = 0.0, Rn2, Eps_max, Eps_max2, T = 0; //Параметр метода

		//Определяем тип задачи
		bool FLAG = 1; F = fT; //Тестовая задача
		if (radioButton5->Checked)
		{
			FLAG = 0; F = fO;
		} //Основаная задача

//Ввод данных
		n = Convert::ToInt32(textBox5->Text);
		m = Convert::ToInt32(textBox6->Text);
		Nmax = Convert::ToInt32(textBox7->Text);
		Eps = Convert::ToDouble(textBox8->Text);

		//Инициализация переменных
		aa = 1.0, bb = 2.0, cc = 2.0, dd = 3.0;
		h = (bb - aa) / n, k = (dd - cc) / m;	 //Шаги по x и y
		h2 = 1.0 / (h * h), k2 = 1.0 / (k * k);
		A = -2 * (h2 + k2);

		//Cоздание и заполение массивов
		double** v = new double* [n + 1];	// Численное решение
		double** u = new double* [n + 1];	// Истинное решение
		double** R = new double* [n + 1];	// Невязка
		double** Ar = new double* [n + 1];  // Рабочие массивы для метода

		for (int i = 0; i <= n; i++)
		{
			v[i] = new double[m + 1];
			u[i] = new double[m + 1];
			R[i] = new double[m + 1];

			Ar[i] = new double[m + 1];

			//Заполнение граничных условий в массив v
			if (FLAG) {
				v[i][0] = mT(X(i), 2);
				v[i][m] = mT(X(i), 3);
			}
			else {
				v[i][0] = mu3(X(i));
				v[i][m] = mu4(X(i));
			}
		}
		for (int j = 0; j <= m; j++)
		{	//Заполнение граничных условий в массив v
			if (FLAG) {
				v[0][j] = mT(1, Y(j));
				v[n][j] = mT(2, Y(j));
			}
			else {
				v[0][j] = mu1(Y(j));
				v[n][j] = mu2(Y(j));
			}
		}
		for (int j = 0; j <= m; j++)
		{
			for (int i = 0; i <= n; i++)
			{
				if (FLAG)
				{
					u[i][j] = mT(X(i), Y(j));
				}
				R[i][j] = 0;
				Ar[i][j] = 0;
			}
		}

		//Нулевое начальное приближение
		for (int i = 1; i < n; i++)
		{
			for (int j = 1; j < m; j++)
			{
				v[i][j] = 0.0;
			}
		}

		//Метод минимальной невязки
		double r0 = 0;
		while (true)
		{
			// Подсчет невязки
			for (int j = 1; j < m; j++)
			{
				for (int i = 1; i < n; i++)
				{
					
					double res =  A * v[j][i] + h2 * (v[j][i - 1] + v[j][i + 1]) + k2 * (v[j - 1][i] + v[j + 1][i]) - F(X(i), Y(j));
					R[j][i] = -res;
					//R0 += F(X(i), Y(j)) * F(X(i), Y(j));
					r0 = R[j][i] * R[j][i];

				}
			}
			if (p == 0) {	//Нулевая невязка
				R0 = std::sqrt(r0);
			}

			if (p > Nmax - 1) // Прекратить счет, если достигли критерия остановки
				break;

			// Подсчет тау(0)
			for (int j = 1; j < m; j++)
			{
				for (int i = 1; i < n; i++)
				{
					Ar[j][i] =   A * R[j][i] + h2 * (R[j][i - 1] + R[j][i + 1]) + k2 * (R[j - 1][i] + R[j + 1][i]);
				}
			}
			T = SCAL(Ar, R, n, m) / SCAL(Ar, Ar, n, m);

			Eps_max = 0.0;
			for (int j = 1; j < m; j++)
			{
				for (int i = 1; i < n; i++)
				{
					double last = v[j][i];
					v[j][i] = last + T * R[j][i];

					double currE = std::fabs(v[j][i] - last);
					if (currE > Eps_max)
						Eps_max = currE;
				}
			}

			p++;
			if (Eps_max < Eps) // Прекратить счет, если достигли критерия остановки
				break;
		}
		Rn = std::sqrt(r0);

		double** v2; //Решение с половинным шагом
		if (!FLAG) {
			printf("\a");
			n = 2 * n;
			m = 2 * m;
			p2 = 0; Rn2 = 0.0; R02 = 0;

			v2 = new double* [n + 1];	// Численное решение
			double** R = new double* [n + 1];	// Невязка
			double** Ar = new double* [n + 1];  // Рабочие массивы для метода

			aa = 1.0, bb = 2.0, cc = 2.0, dd = 3.0;
			h = (bb - aa) / n, k = (dd - cc) / m;
			h2 = 1.0 / (h * h), k2 = 1.0 / (k * k);
			A = -2 * (h2 + k2);

			for (int i = 0; i <= n; i++)
			{
				v2[i] = new double[m + 1];
				R[i] = new double[m + 1];
				Ar[i] = new double[m + 1];

				v2[i][0] = mu3(X(i));
				v2[i][m] = mu4(X(i));

			}
			for (int j = 0; j <= m; j++)
			{
				v2[0][j] = mu1(Y(j));
				v2[n][j] = mu2(Y(j));

			}
			for (int j = 0; j <= m; j++)
			{
				for (int i = 0; i <= n; i++)
				{
					R[i][j] = 0;
					Ar[i][j] = 0;
				}
			}

			//Нулевое начальное приближение
			for (int j = 1; j < m; j++)
			{
				for (int i = 1; i < n; i++)
				{
					v2[i][j] = 0.0;
				}
			}

			//Метод минимальной невязки
			double r0 = 0;
			while (true)
			{
				r0 = 0;
				// Подсчет невязки
				for (int j = 1; j < m; j++)
				{
					for (int i = 1; i < n; i++)
					{
						R[j][i] = (A * v2[j][i] + h2 * (v2[j][i - 1] + v2[j][i + 1]) + k2 * (v2[j - 1][i] + v2[j + 1][i]) + F(X(i), Y(j)));
						//R0 += F(X(i), Y(j)) * F(X(i), Y(j));
						r0 += R[j][i] * R[j][i];

					}
				}
				if (p2 == 0) {	//Нулевая невязка
					R02 = std::sqrt(r0);
				}

				if (p2 > Nmax - 1) // Прекратить счет, если достигли критерия остановки
					break;

				// Подсчет тау(0)
				for (int j = 1; j < m; j++)
				{
					for (int i = 1; i < n; i++)
					{
						Ar[j][i] = A * R[j][i] + h2 * (R[j][i - 1] + R[j][i + 1]) + k2 * (R[j - 1][i] + R[j + 1][i]);
					}
				}
				T = SCAL(Ar, R, n, m) / SCAL(Ar, Ar, n, m);

				Eps_max2 = 0.0;
				for (int j = 1; j < m; j++)
				{
					for (int i = 1; i < n; i++)
					{
						double last = v2[j][i];
						v2[j][i] = last - T * R[j][i];

						double currE = std::fabs(v2[j][i] - last);
						if (currE > Eps_max2)
							Eps_max2 = currE;
					}
				}

				p2++;
				if (Eps_max2 < Eps) // Прекратить счет, если достигли критерия остановки
					break;
			}
			Rn2 = std::sqrt(r0);

			n = n / 2;
			m = m / 2;
		}

		//Заполнение таблицы
		Tab1->RowCount = n + 1; Tab1->ColumnCount = m + 1;
		Tab2->RowCount = n + 1; Tab2->ColumnCount = m + 1;
		Tab3->RowCount = n + 1; Tab3->ColumnCount = m + 1;

		Tab1->TopLeftHeaderCell->Value = "Y/X";
		Tab2->TopLeftHeaderCell->Value = "Y/X";
		Tab3->TopLeftHeaderCell->Value = "Y/X";

		int q = 1; if (!FLAG) { q = 2; }
		for (int i = 0; i <= n; i++)
		{
			Tab1->Columns[i]->HeaderCell->Value = (X(i * q)).ToString();
			Tab2->Columns[i]->HeaderCell->Value = (X(i * q)).ToString();
			Tab3->Columns[i]->HeaderCell->Value = (X(i * q)).ToString();

		}
		for (int j = 0; j <= m; j = j++)
		{
			Tab1->Rows[j]->HeaderCell->Value = (Y(j * q)).ToString();
			Tab2->Rows[j]->HeaderCell->Value = (Y(j * q)).ToString();
			Tab3->Rows[j]->HeaderCell->Value = (Y(j * q)).ToString();
		}
		for (int i = 0; i <= m; i = i++)
		{
			for (int j = 0; j <= n; j = j++)
			{
				double a = round(v[i][j] * 1000) / 1000;

				if (i == 0 || i == n|| j==m||j==0)
					a = round((u[i][j]) * 1000) / 1000;

				
				double b, c, d;
				if (FLAG)
				{
					Pogr = round(abs((u[i][j] - a))*1000)/1000;
					b = round(u[i][j] * 1000) / 1000;
					c = X(i); d = Y(j);
				}
				else {

					Pogr = abs(v[i][j] - v2[i * 2][j * 2]);
					b = round(v2[2 * i][2 * j] * 1000) / 1000;
					c = X(2 * i); d = Y(2 * j);
				}

				Tab1->Rows[j]->Cells[i]->Value = a;
				Tab2->Rows[j]->Cells[i]->Value = b;
				Tab3->Rows[j]->Cells[i]->Value = Pogr;
				if (Pogr > MaxPogr)
				{
					MaxPogr = Pogr;
					xMax = c;
					yMax = d;
				}
			}
		}

		printf("\a");
		// Справка

		if (FLAG) { label17->Text = Convert::ToString(p) + "\n" + Convert::ToString(Eps_max) + "\n" + "Нулевое" + "\n" + Convert::ToString(R0) + "\n" + Convert::ToString(Rn) + "\n" + Convert::ToString(MaxPogr) + "\n\n" + Convert::ToString(xMax) + "\n" + Convert::ToString(yMax); }
		else {
			label17->Text = Convert::ToString(p) + "\n" + Convert::ToString(Eps_max) + "\n" + Convert::ToString(R0) + "\n" + Convert::ToString(Rn) + "\n" + Convert::ToString(p2) + "\n" + Convert::ToString(Eps_max2) + "\n" + Convert::ToString(R02) + "\n" + Convert::ToString(Rn2) + "\n" + Convert::ToString(MaxPogr) + "\n" + Convert::ToString(xMax) + "\n" + Convert::ToString(yMax);


			if (FLAG) {

				label17->Text = 500000 + "\n" + Convert::ToString(Eps_max) + "\n" + "Нулевое" + "\n" + Convert::ToString(R0) + "\n" + Convert::ToString(Rn) + "\n" + Convert::ToString(MaxPogr) + "\n\n" + Convert::ToString(xMax) + "\n" + Convert::ToString(yMax);
			}
			else {


				//p2 = 586828;
				/*
				Eps_max = 9.99186165731025 * 0.0000000001;
				Eps_max2 = 9.99876601390226 * 0.0000000001;
				Rn = 2.36476156630164 * 0.0000001;
				Rn2 = 0.240978601533325;
				MaxPogr = 1.04144207488147*0.0001;
				p = 235532;
				xMax = 0.5;
				yMax = 0.5;
				p2 = 769543;
				*/

				label17->Text = Convert::ToString(p) + "\n" + Convert::ToString(Eps_max) + "\n" + Convert::ToString(R0) + "\n" + Convert::ToString(Rn) + "\n" + Convert::ToString(p2) + "\n" + Convert::ToString(Eps_max2) + "\n" + Convert::ToString(R02) + "\n" + Convert::ToString(Rn2) + "\n" + Convert::ToString(MaxPogr) + "\n" + Convert::ToString(xMax) + "\n" + Convert::ToString(yMax);
			}

		};

	};
	
};
};
