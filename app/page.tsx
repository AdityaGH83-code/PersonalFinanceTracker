import ExpenseForm from '../components/ExpenseForm';
import ExpenseList from '../components/ExpenseList';
import Chart from '../components/Chart';
import Insights from '../components/Insights';

export default function Home() {
  return (
    <div className="container mx-auto p-4">
      <h1 className="text-2xl font-bold mb-4">Expense Tracker with Budget Insights</h1>
      <ExpenseForm />
      <Chart />
      <Insights />
      <ExpenseList />
    </div>
  );
}
