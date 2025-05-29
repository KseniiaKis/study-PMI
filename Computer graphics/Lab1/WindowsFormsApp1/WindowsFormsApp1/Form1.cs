using Filters;

using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Net.NetworkInformation;
using System.Runtime.InteropServices;
using System.Security.Policy;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace WindowsFormsApp1
{
    public partial class Form1 : Form
    {
        Bitmap image;

        bool[,] kernel = { { false, true, false }, { true, true, true }, { false, true, false } };
        public Form1()
        {
            InitializeComponent();
        }

        private void открытьToolStripMenuItem_Click(object sender, EventArgs e)
        {
            OpenFileDialog dialoge = new OpenFileDialog();
            dialoge.Filter = "Image files | *.png; *.jpg; *.bpm | All Files (*.*) | (*.*)";
            if (dialoge.ShowDialog() == DialogResult.OK)
            {
                image = new Bitmap(dialoge.FileName);
                pictureBox1.Image = image;
                pictureBox1.Refresh();
            }
        }

        private void инверсияToolStripMenuItem_Click(object sender, EventArgs e)
        {
            backgroundWorker1.RunWorkerAsync(new InvertFilter());
        }

        private void button1_Click(object sender, EventArgs e)
        {
            backgroundWorker1.CancelAsync();
        }

        private void backgroundWorker1_DoWork(object sender, DoWorkEventArgs e)
        {
            Bitmap newImage = ((Filters_)e.Argument).processImage(image, backgroundWorker1);
            if (!backgroundWorker1.CancellationPending)
                image = newImage;
        }

        private void backgroundWorker1_ProgressChanged(object sender, ProgressChangedEventArgs worker)
        {
            progressBar1.Value = worker.ProgressPercentage;
        }

        private void backgroundWorker1_RunWorkerCompleted(object sender, RunWorkerCompletedEventArgs worker)
        {
            if (!worker.Cancelled)
            {
                pictureBox1.Image = image;
                pictureBox1.Refresh();
            }
            progressBar1.Value = 0;
        }

        private void размытиеToolStripMenuItem_Click(object sender, EventArgs e)
        {
            Filters_ filter = new BlurFilter();
            backgroundWorker1.RunWorkerAsync(filter);
        }

        private void ГаусToolStripMenuItem_Click(object sender, EventArgs e)
        {
            Filters_ filter = new GaussianFilter();
            backgroundWorker1.RunWorkerAsync(filter);
        }

        private void ЧБToolStripMenuItem_Click(object sender, EventArgs e)
        {
            Filters_ filter = new GrayScaleFilter();
            backgroundWorker1.RunWorkerAsync(filter);
        }

        private void сепияToolStripMenuItem_Click(object sender, EventArgs e)
        {
            Filters_ filter = new SepiaFilter();
            backgroundWorker1.RunWorkerAsync(filter);
        }

        private void яркостьToolStripMenuItem_Click(object sender, EventArgs e)
        {
            Filters_ filter = new BrightnessFilter();
            backgroundWorker1.RunWorkerAsync(filter);
        }

        private void собельToolStripMenuItem_Click(object sender, EventArgs e)
        {
            Filters_ filter = new SobelFilter();
            backgroundWorker1.RunWorkerAsync(filter);
        }

        private void резкостьToolStripMenuItem_Click(object sender, EventArgs e)
        {
            Filters_ filter = new SharpnessFilter();
            backgroundWorker1.RunWorkerAsync(filter);
        }

        private void серыйМирToolStripMenuItem_Click_1(object sender, EventArgs e)
        {
            Filters_ filter = new GrayWorldFilter();
            backgroundWorker1.RunWorkerAsync(filter);
        }

        private void стеклоToolStripMenuItem_Click(object sender, EventArgs e)
        {
            Filters_ filter = new GlassFilter();
            backgroundWorker1.RunWorkerAsync(filter);
        }

        private void переносToolStripMenuItem_Click(object sender, EventArgs e)
        {
            Filters_ filter = new RelocateFilter();
            backgroundWorker1.RunWorkerAsync(filter);
        }

        private void поворотToolStripMenuItem_Click(object sender, EventArgs e)
        {
            Filters_ filter = new TurnFilter();
            backgroundWorker1.RunWorkerAsync(filter);
        }

        private void медианныйФильтрToolStripMenuItem_Click(object sender, EventArgs e)
        {
            Filters_ filter = new MedianFilter();
            backgroundWorker1.RunWorkerAsync(filter);
        }

        private void расширениеToolStripMenuItem_Click(object sender, EventArgs e)
        {
            Filters_ filter = new DilationFilter(kernel);
            backgroundWorker1.RunWorkerAsync(filter);
        }

        private void эрозияToolStripMenuItem_Click(object sender, EventArgs e)
        {
            Filters_ filter = new ErosionFilter(kernel);
            backgroundWorker1.RunWorkerAsync(filter);
        }

        private void открытиеToolStripMenuItem_Click(object sender, EventArgs e)
        {
            Filters_ filter = new OpeningFilter(kernel);
            backgroundWorker1.RunWorkerAsync(filter);
        }

        private void закрытиеToolStripMenuItem_Click(object sender, EventArgs e)
        {
            Filters_ filter = new ClosingFilter(kernel);
            backgroundWorker1.RunWorkerAsync(filter);
        }

        private void градиентToolStripMenuItem_Click(object sender, EventArgs e)
        {
            Filters_ filter = new GradFilter(kernel);
            backgroundWorker1.RunWorkerAsync(filter);
        }

        private void линейноеРастяжГистограммыToolStripMenuItem_Click(object sender, EventArgs e)
        {
            Filters_ filter = new LinearHistogramStretchingFilter();
            backgroundWorker1.RunWorkerAsync(filter);
        }

        private void toolStripMenuItem2_Click(object sender, EventArgs e)
        {
            Filters_ filter = new WaveFilter1();
            backgroundWorker1.RunWorkerAsync(filter);
        }

        private void toolStripMenuItem3_Click(object sender, EventArgs e)
        {
            Filters_ filter = new WaveFilter2();
            backgroundWorker1.RunWorkerAsync(filter);
            
        }

        private void toolStripMenuItem4_Click(object sender, EventArgs e)
        {
            Filters_ filter = new SharraFilter();
            backgroundWorker1.RunWorkerAsync(filter);   
        }

        private void toolStripMenuItem5_Click(object sender, EventArgs e)
        {
            Filters_ filter = new PriuttaFilter();
            backgroundWorker1.RunWorkerAsync(filter);
        }

        private void motionBlurToolStripMenuItem_Click(object sender, EventArgs e)
        {
            Filters_ filter = new MotionBlur();
            backgroundWorker1.RunWorkerAsync(filter);
            
        }

        private void допToolStripMenuItem_Click(object sender, EventArgs e)
        {
            Filters_ filter = new Task1();
            backgroundWorker1.RunWorkerAsync(filter);
        }
    }
}

namespace Filters
{
    abstract class Filters_
    {
        protected abstract Color calculateNewPixelColor(Bitmap sourceImage, int i, int j);
        public virtual Bitmap processImage(Bitmap sourceImage, BackgroundWorker worker)
        {
            Bitmap resultImage = new Bitmap(sourceImage.Width, sourceImage.Height);
            for (int i = 0; i < sourceImage.Width; i++)
            {
                for (int j = 0; j < sourceImage.Height; j++)
                {
                    resultImage.SetPixel(i, j, calculateNewPixelColor(sourceImage, i, j));
                }
                worker.ReportProgress((int)((float)i / resultImage.Width * 100));
                if (worker.CancellationPending)
                    return null;
                
            }
            return resultImage;
        }

        public int Clamp(int value, int min, int max)
        {
            if (value < min)
                return min;
            if (value > max)
                return max;
            return value;
        }
    }

    class MotionBlur : MatrixFilter
    {
        public void createMotionBlurCernel(int n)
        {
            int size = n;
            kernel = new float[size, size];

            for (int i = 0; i < size; i++)
                for (int j = 0; j < size; j++)
                {
                    if (i == j)
                        kernel[i, j] = ((float)1 / n);
                    else
                        kernel[i, j] = 0;
                }
        }

        public MotionBlur()
        {
            createMotionBlurCernel(9);
        }
    }

    class MatrixFilter : Filters_
    {
        protected float[,] kernel = null;
        protected MatrixFilter() { }
        public MatrixFilter(float[,] kernel)
        {
            this.kernel = kernel;
        }
        protected override Color calculateNewPixelColor(Bitmap sourceImage, int x, int y)
        {
            int radiusX = kernel.GetLength(0) / 2;
            int radiusY = kernel.GetLength(1) / 2;

            float resultR = 0;
            float resultG = 0;
            float resultB = 0;
            for (int l = -radiusY; l <= radiusY; l++)
            {
                for (int k = -radiusX; k <= radiusX; k++)
                {
                    int idX = Clamp(x + k, 0, sourceImage.Width - 1);
                    int idY = Clamp(y + l, 0, sourceImage.Height - 1);
                    Color neighborColor = sourceImage.GetPixel(idX, idY);
                    resultR += neighborColor.R * kernel[k + radiusX, l + radiusY];
                    resultG += neighborColor.G * kernel[k + radiusX, l + radiusY];
                    resultB += neighborColor.B * kernel[k + radiusX, l + radiusY];
                }
            }
            return Color.FromArgb(
                Clamp((int)resultR, 0, 255),
                Clamp((int)resultG, 0, 255),
                Clamp((int)resultB, 0, 255)
                );
        }
    }

    class MathMorphology : Filters_
    {
        protected bool isDilation;
        protected bool[,] kernel = null;

        protected MathMorphology()
        {
        }

        public MathMorphology(bool[,] kernel)
        {
            this.kernel = kernel;
        }

        protected override Color calculateNewPixelColor(Bitmap sourceImage, int x, int y)
        {
            int max = 0;
            int min = int.MaxValue;
            Color clr = Color.Black;
            int radiusX = kernel.GetLength(0) / 2;
            int radiusY = kernel.GetLength(1) / 2;
            for (int l = -radiusY; l <= radiusY; l++)
                for (int k = -radiusX; k <= radiusX; k++)
                {
                    int idX = Clamp(x + k, 0, sourceImage.Width - 1);
                    int idY = Clamp(y + l, 0, sourceImage.Height - 1);
                    Color sourceColor = sourceImage.GetPixel(idX, idY);
                    int intensity = (int)(0.36 * sourceColor.R + 0.53 * sourceColor.G + 0.11 * sourceColor.B);
                    if (isDilation)
                    {
                        if ((kernel[k + radiusX, l + radiusY]) && (intensity > max))
                        {
                            max = intensity;
                            clr = sourceColor;
                        }
                    }
                    else
                    {
                        if (intensity < min)
                        {
                            min = intensity;
                            clr = sourceColor;
                        }
                    }
                }

            return clr;
        }

    }


    class InvertFilter : Filters_
    {
        protected override Color calculateNewPixelColor(Bitmap sourceImage, int x, int y)
        {
            Color sourceColor = sourceImage.GetPixel(x, y);
            Color resultColor = Color.FromArgb(255 - sourceColor.R, 255 - sourceColor.G, 255 - sourceColor.B);
            return resultColor;
        }
    }

    class GlassFilter : Filters_
    {

        protected override Color calculateNewPixelColor(Bitmap sourceImage, int k, int l)
        {
            int x, y;

            Random rnd1 = new Random();
            y = (int)(l + (rnd1.NextDouble() - 0.5) * 10);

            Random rnd = new Random();
            x = (int)(k + (rnd.NextDouble() - 0.5) * 10);

            return sourceImage.GetPixel(Clamp(x, 0, sourceImage.Width - 1), Clamp(y, 0, sourceImage.Height - 1));
        }


    }

    class WaveFilter1 : Filters_
    {
        protected override Color calculateNewPixelColor(Bitmap sourceImage, int x, int y)
        {
            int newX, newY;
            newX = Clamp((int)(x + 20 * Math.Sin(2 * Math.PI * y / 60)), 0, sourceImage.Width - 1);
            newY = Clamp(y, 0, sourceImage.Height - 1);
            Color sourceColor = sourceImage.GetPixel(newX, newY);
            Color resultColor = Color.FromArgb(sourceColor.R, sourceColor.G, sourceColor.B);

            return resultColor;
        }
    }

    class WaveFilter2 : Filters_
    {
        protected override Color calculateNewPixelColor(Bitmap sourceImage, int x, int y)
        {
            int newX, newY;
            newX = Clamp((int)(x + 20 * Math.Sin(2 * Math.PI * x / 30)), 0, sourceImage.Width - 1);
            newY = Clamp(y, 0, sourceImage.Height - 1);
            Color sourceColor = sourceImage.GetPixel(newX, newY);
            Color resultColor = Color.FromArgb(sourceColor.R, sourceColor.G, sourceColor.B);

            return resultColor;
        }
    }

    class GrayWorldFilter : Filters_
    {
        protected override Color calculateNewPixelColor(Bitmap sourceImage, int x, int y)
        {
            Color sourceColor = sourceImage.GetPixel(x, y);

            double N = sourceImage.Width*sourceImage.Height;

            double R_ = 0;
            double G_ = 0;
            double B_ = 0;

                
            R_ = R_ + sourceColor.R;
            G_ = G_ + sourceColor.G;
            B_ = B_ + sourceColor.B;
 

            R_ = R_ / N;
            G_ = G_ / N;
            B_ = B_ / N;

            double Avg = (R_ + G_ + B_) / 3;

            double resultR = sourceColor.R * (Avg / R_);
            double resultG = sourceColor.G * (Avg / G_);
            double resultB = sourceColor.B * (Avg / B_);

            
            Color resultColor = Color.FromArgb(Clamp((int)resultR, 0, 255), 
                                               Clamp((int)resultG, 0, 255),
                                               Clamp((int)resultB, 0, 255));
            return resultColor;
        }
    }

    class GrayScaleFilter : Filters_
    {
        protected override Color calculateNewPixelColor(Bitmap sourceImage, int x, int y)
        {
            Color sourceColor = sourceImage.GetPixel(x, y);
            int tmp = (int)(0.36 * sourceColor.R + 0.53 * sourceColor.G + 0.11 * sourceColor.B);
            Color resultColor = Color.FromArgb(tmp, tmp, tmp);
            return resultColor;
        }
    }

    class SepiaFilter : Filters_
    {
        protected override Color calculateNewPixelColor(Bitmap sourceImage, int x, int y)
        {
            Color sourceColor = sourceImage.GetPixel(x, y);
            int k = 10;
            int tmp = (int)(0.36 * sourceColor.R + 0.53 * sourceColor.G + 0.11 * sourceColor.B);

            float resultR = tmp + 2 * k;
            float resultG = (float)(tmp + 0.5 * k);
            float resultB = tmp - k;

            return Color.FromArgb(
                Clamp((int)resultR, 0, 255),
                Clamp((int)resultG, 0, 255),
                Clamp((int)resultB, 0, 255)
                );
        }
    }
    class BrightnessFilter : Filters_
    {
        protected override Color calculateNewPixelColor(Bitmap sourceImage, int x, int y)
        {
            Color sourceColor = sourceImage.GetPixel(x, y);
            int k = 30;

            float resultR = sourceColor.R + k;
            float resultG = sourceColor.G + k;
            float resultB = sourceColor.B + k;

            return Color.FromArgb(
                Clamp((int)resultR, 0, 255),
                Clamp((int)resultG, 0, 255),
                Clamp((int)resultB, 0, 255)
                );
        }
    }

    class RelocateFilter : Filters_
    {
        protected override Color calculateNewPixelColor(Bitmap sourceImage, int x, int y)
        {

            int newX = x + 50;

            if (newX >= 0 && newX < sourceImage.Width)
            {
                return sourceImage.GetPixel(newX, y);
            }
            else
            {
                return Color.Black;
            }
        }
    }
    class TurnFilter : Filters_
    {
        protected override Color calculateNewPixelColor(Bitmap sourceImage, int x, int y)
        {
            int midX = sourceImage.Width / 2;
            int midY = sourceImage.Height / 2;
            double mu = Math.PI / 6;

            int newX = (int)((x - midX) * Math.Cos(mu) - (y - midY) * Math.Sin(mu) + midX);
            int newY = (int)((x - midX) * Math.Sin(mu) + (y - midY) * Math.Cos(mu) + midY);

            if (newX >= 0 && newX < sourceImage.Width && newY >= 0 && newY < sourceImage.Height)
            {
                return sourceImage.GetPixel(newX, newY);
            }
            else
            {
                return Color.Black;
            }
        }
    }

    class BlurFilter : MatrixFilter
    {
        public BlurFilter()
        {
            int sizeX = 3;
            int sizeY = 3;
            kernel = new float[sizeX, sizeY] ;
            for (int i = 0; i < sizeX; i++)
                for (int j = 0; j < sizeY; j++)
                    if (i == j)
                        kernel[i, j] = 1.0f;
                    else
                        kernel[i, j] = 0;
        }
    }

    class GaussianFilter : MatrixFilter
    {
        public GaussianFilter() { createGaussianFilterKernel(7, 2); }

        public void createGaussianFilterKernel(int radius, float sigma)
        {
            int size = 2 * radius + 1;
            kernel = new float[size, size];
            float norm = 0;
            for (int i = -radius; i <= radius; i++)
                for (int j = -radius; j <= radius; j++)
                {
                    kernel[i + radius, j + radius] = (float)(Math.Exp(-(i * i + j * j) / (sigma * sigma)));
                    norm += kernel[i + radius, j + radius];
                }
            for (int i = 0; i < size; i++)
                for (int j = 0; j < size; j++)
                    kernel[i, j] /= norm;
        }
    }

    class SobelFilter : MatrixFilter
    {
        public SobelFilter() { createSobelFilterKernel(3, 2); }

        public void createSobelFilterKernel(int radius, float sigma)
        {
            int size = 3;
            kernel = new float[size, size];

            int i = 0; 
            kernel[i, 0] = -1;
            kernel[i, 1] = -2;
            kernel[i, 2] = -1;

            for ( i = 0; i < size; i++ )
            {
                kernel[1, i] = 0;
            }

            i = 2;
            kernel[i, 0] = 1;
            kernel[i, 1] = 2;
            kernel[i, 2] = 1;

            Console.WriteLine(kernel);
        }
    }

    class SharpnessFilter : MatrixFilter
    {
        public SharpnessFilter() { createSharpnessFilterKernel(3, 2); }

        public void createSharpnessFilterKernel(int radius, float sigma)
        {
            int size = 3;
            kernel = new float[size, size];

            int i = 0;
            for (i = 0; i<size; i = i+2)
            {
                kernel[i, 0] = -1;
                kernel[i, 1] = -1;
                kernel[i, 2] = -1; 
            }


            i = 1;
            kernel[i, 0] = -1;
            kernel[i, 1] = 9;
            kernel[i, 2] = -1;
        }
    }

    class LinearHistogramStretchingFilter : Filters_
    {
        private int minIntensity = 255;
        private int maxIntensity = 0;
        protected override Color calculateNewPixelColor(Bitmap sourceImage, int x, int y)
        {
            if((x == 0) && (y == 0))
            {
                CalculateMinMaxValues(sourceImage);
            }

            Color pixelColor = sourceImage.GetPixel(x, y);
            int intensity = (int)(0.299 * pixelColor.R + 0.587 * pixelColor.G + 0.114 * pixelColor.B);

            int newIntensity = (int)((255.0 / (maxIntensity - minIntensity)) * (intensity - minIntensity));
            newIntensity = Clamp(newIntensity, 0, 255);

            int newRed = pixelColor.R * newIntensity / intensity;
            int newGreen = pixelColor.G * newIntensity / intensity;
            int newBlue = pixelColor.B * newIntensity / intensity;

            return Color.FromArgb(Clamp(newRed, 0, 255), Clamp(newGreen, 0, 255), Clamp(newBlue, 0, 255));

        }

        private void CalculateMinMaxValues(Bitmap sourceImage)
        {
            for (int i = 0; i < sourceImage.Width; i++)
            {
                for (int j = 0; j < sourceImage.Height; j++)
                {
                    Color srcColor = sourceImage.GetPixel(i, j);
                    int srcIntensity = (int)(0.299 * srcColor.R + 0.587 * srcColor.G + 0.114 * srcColor.B);

                    if (srcIntensity < minIntensity)
                        minIntensity = srcIntensity;
                    if (srcIntensity > maxIntensity)
                        maxIntensity = srcIntensity;
                }
            }
        }
    }

    class Task1 : Filters_
    {
        private int minIntensity = 255;
        private int maxIntensity = 0;

        protected override Color calculateNewPixelColor(Bitmap sourceImage, int x, int y)
        {

            Color pixelColor = sourceImage.GetPixel(x, y);

            int intensity = (int)(0.36 * pixelColor.R) + (int)(0.53 * pixelColor.G) + (int)(0.11 * pixelColor.B);

            if (intensity <= 100)
                return Color.FromArgb(0, 0, 255);
            else if ((intensity > 100) && (intensity <= 200))
                return Color.FromArgb(168, 216, 255);
            else
                return Color.FromArgb(255, 255, 255);

        }
    }

    class MedianFilter : Filters_
    {
        protected override Color calculateNewPixelColor(Bitmap sourceImage, int x, int y)
        {
            int radius = 3;
            int size = 2 * radius + 1;
            int[] redValues = new int[size * size];
            int[] greenValues = new int[size * size];
            int[] blueValues = new int[size * size];
            int index = 0;

            for (int i = -radius; i <= radius; i++)
            {
                for (int j = -radius; j <= radius; j++)
                {
                    int newX = Clamp(x + i, 0, sourceImage.Width - 1);
                    int newY = Clamp(y + j, 0, sourceImage.Height - 1);
                    Color neighborColor = sourceImage.GetPixel(newX, newY);
                    redValues[index] = neighborColor.R;
                    greenValues[index] = neighborColor.G;
                    blueValues[index] = neighborColor.B;
                    index++;
                }
            }

            Array.Sort(redValues);
            Array.Sort(greenValues);
            Array.Sort(blueValues);

            int medianIndex = size * size / 2;

            return Color.FromArgb(Clamp(redValues[medianIndex], 0, 255), Clamp(greenValues[medianIndex], 0, 255), Clamp(blueValues[medianIndex], 0, 255));
        }
    }

    class PriuttaFilter : Filters_
    {
        float[,] kernelX = { { -1, -1, -1 }, { 0, 0, 0 }, { 1, 1, 1 } };

        float[,] kernelY = { { -1, 0, 1 }, { -1, 0, 1 }, { -1, 0, 1 } };

        public PriuttaFilter()
        {
        }

        protected override Color calculateNewPixelColor(Bitmap sourceImage, int x, int y)
        {
            int radiusX = kernelX.GetLength(0) / 2;
            int radiusY = kernelY.GetLength(1) / 2;

            float resultRX = 0;
            float resultGX = 0;
            float resultBX = 0;

            float resultRY = 0;
            float resultGY = 0;
            float resultBY = 0;

            for (int l = -radiusY; l <= radiusY; l++)
            {
                for (int k = -radiusX; k <= radiusX; k++)
                {
                    int idX = Clamp(x + k, 0, sourceImage.Width - 1);
                    int idY = Clamp(y + l, 0, sourceImage.Height - 1);

                    Color neighborColor = sourceImage.GetPixel(idX, idY);

                    resultRX += neighborColor.R * kernelX[k + radiusX, l + radiusY];
                    resultGX += neighborColor.G * kernelX[k + radiusX, l + radiusY];
                    resultBX += neighborColor.B * kernelX[k + radiusX, l + radiusY];

                    resultRY += neighborColor.R * kernelX[k + radiusX, l + radiusY];
                    resultGY += neighborColor.G * kernelX[k + radiusX, l + radiusY];
                    resultBY += neighborColor.B * kernelX[k + radiusX, l + radiusY];
                }
            }

            int newR = (int)(Math.Sqrt(Math.Pow(resultRX, 2) + Math.Pow(resultRY, 2)));
            int newG = (int)(Math.Sqrt(Math.Pow(resultGX, 2) + Math.Pow(resultGY, 2)));
            int newB = (int)(Math.Sqrt(Math.Pow(resultBX, 2) + Math.Pow(resultBY, 2)));

            return Color.FromArgb(Clamp(newR, 0, 255), Clamp(newG, 0, 255), Clamp(newB, 0, 255));
        }
    }

    class SharraFilter : Filters_
    {
        float[,] kernelX = { { 3, 10, 3 }, { 0, 0, 0 }, { -3, -10, -3 } };

        float[,] kernelY = { { 3, 0, -3 }, { 10, 0, -10 }, { 3, 0, -3 } };

        public SharraFilter()
        {
        }

        protected override Color calculateNewPixelColor(Bitmap sourceImage, int x, int y)
        {
            int radiusX = kernelX.GetLength(0) / 2;
            int radiusY = kernelY.GetLength(1) / 2;

            float resultRX = 0;
            float resultGX = 0;
            float resultBX = 0;

            float resultRY = 0;
            float resultGY = 0;
            float resultBY = 0;

            for (int l = -radiusY; l <= radiusY; l++)
            {
                for (int k = -radiusX; k <= radiusX; k++)
                {
                    int idX = Clamp(x + k, 0, sourceImage.Width - 1);
                    int idY = Clamp(y + l, 0, sourceImage.Height - 1);

                    Color neighborColor = sourceImage.GetPixel(idX, idY);

                    resultRX += neighborColor.R * kernelX[k + radiusX, l + radiusY];
                    resultGX += neighborColor.G * kernelX[k + radiusX, l + radiusY];
                    resultBX += neighborColor.B * kernelX[k + radiusX, l + radiusY];

                    resultRY += neighborColor.R * kernelX[k + radiusX, l + radiusY];
                    resultGY += neighborColor.G * kernelX[k + radiusX, l + radiusY];
                    resultBY += neighborColor.B * kernelX[k + radiusX, l + radiusY];
                }
            }

            int newR = (int)(Math.Sqrt(Math.Pow(resultRX, 2) + Math.Pow(resultRY, 2)));
            int newG = (int)(Math.Sqrt(Math.Pow(resultGX, 2) + Math.Pow(resultGY, 2)));
            int newB = (int)(Math.Sqrt(Math.Pow(resultBX, 2) + Math.Pow(resultBY, 2)));

            return Color.FromArgb(Clamp(newR, 0, 255), Clamp(newG, 0, 255), Clamp(newB, 0, 255));
        }
    }

    class DilationFilter : MathMorphology
    {
        public DilationFilter(bool[,] _kernel)
        {
            isDilation = true;
            this.kernel = _kernel;
        }
    }

    class ErosionFilter : MathMorphology
    {
        public ErosionFilter(bool[,] _kernel)
        {
            isDilation = false;
            this.kernel = _kernel;
        }
    }

    class OpeningFilter : MathMorphology
    {
        public OpeningFilter(bool[,] _kernel)
        {
            this.kernel = _kernel;
        }

        public override Bitmap processImage(Bitmap sourceImage, BackgroundWorker worker)
        {
            Bitmap currImage = new Bitmap(sourceImage.Width, sourceImage.Height);
            Bitmap resultImage = new Bitmap(sourceImage.Width, sourceImage.Height);
            isDilation = false;
            for (int i = 0; i < sourceImage.Width; i++)
            {
                worker.ReportProgress((int)((float)i / resultImage.Width * 100));
                for (int j = 0; j < sourceImage.Height; j++)
                {
                    currImage.SetPixel(i, j, calculateNewPixelColor(sourceImage, i, j));
                }
            }
            isDilation = true;
            for (int i = 0; i < currImage.Width; i++)
            {
                worker.ReportProgress((int)((float)i / resultImage.Width * 100));
                for (int j = 0; j < currImage.Height; j++)
                {
                    resultImage.SetPixel(i, j, calculateNewPixelColor(currImage, i, j));
                }
            }
            return resultImage;
        }
    }

    class ClosingFilter : MathMorphology
    {
        public ClosingFilter(bool[,] _kernel)
        {
            this.kernel = _kernel;
        }

        public override Bitmap processImage(Bitmap sourceImage, BackgroundWorker worker)
        {
            Bitmap currImage = new Bitmap(sourceImage.Width, sourceImage.Height);
            Bitmap resultImage = new Bitmap(sourceImage.Width, sourceImage.Height);
            isDilation = true;
            for (int i = 0; i < sourceImage.Width; i++)
            {
                worker.ReportProgress((int)((float)i / resultImage.Width * 100));
                for (int j = 0; j < sourceImage.Height; j++)
                {
                    currImage.SetPixel(i, j, calculateNewPixelColor(sourceImage, i, j));
                }
            }
            isDilation = false;
            for (int i = 0; i < currImage.Width; i++)
            {
                worker.ReportProgress((int)((float)i / resultImage.Width * 100));
                for (int j = 0; j < currImage.Height; j++)
                {
                    resultImage.SetPixel(i, j, calculateNewPixelColor(currImage, i, j));
                }
            }
            return resultImage;
        }
    }

    class GradFilter : MathMorphology
    {
        public GradFilter(bool[,] _kernel)
        {
            isDilation = true;
            this.kernel = _kernel;
        }

        protected override Color calculateNewPixelColor(Bitmap sourceImage, int x, int y)
        {
            int max = 0;
            int min = int.MaxValue;
            Color gradColor = Color.Black;
            int radiusX = kernel.GetLength(0) / 2;
            int radiusY = kernel.GetLength(1) / 2;

            for (int l = -radiusY; l <= radiusY; l++)
            {
                for (int k = -radiusX; k <= radiusX; k++)
                {
                    int idX = Clamp(x + k, 0, sourceImage.Width - 1);
                    int idY = Clamp(y + l, 0, sourceImage.Height - 1);

                    Color sourceColor = sourceImage.GetPixel(idX, idY);
                    int intensity = (int)(0.36 * sourceColor.R + 0.53 * sourceColor.G + 0.11 * sourceColor.B);

                    if ((kernel[k + radiusX, l + radiusY]) && (intensity > max))
                    {
                        max = intensity;
                        gradColor = sourceColor;
                    }

                    if (intensity < min)
                    {
                        min = intensity;
                    }
                }
            }

            int gradIntensity = Clamp(max - min, 0, 255);

            return Color.FromArgb(gradIntensity, gradIntensity, gradIntensity);
        }
    }
}