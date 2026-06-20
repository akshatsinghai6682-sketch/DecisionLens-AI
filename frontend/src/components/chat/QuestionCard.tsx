import React, { useState } from 'react';
import { ChevronDown } from 'lucide-react';

interface QuestionCardProps {
  question: string;
  examples: string;
  category: string;
  onAnswer: (answer: string) => void;
  isLoading?: boolean;
}

export const QuestionCard: React.FC<QuestionCardProps> = ({
  question,
  examples,
  category,
  onAnswer,
  isLoading = false,
}) => {
  const [isExpanded, setIsExpanded] = useState(false);
  const [answer, setAnswer] = useState('');

  const handleSubmit = () => {
    if (answer.trim()) {
      onAnswer(answer);
      setAnswer('');
    }
  };

  return (
    <div className="bg-white rounded-lg shadow-lg p-6 max-w-2xl mx-auto">
      <div className="mb-4">
        <span className="text-xs font-semibold text-blue-600 uppercase">{category}</span>
        <h2 className="text-xl font-bold text-gray-900 mt-2">{question}</h2>
      </div>

      <button
        onClick={() => setIsExpanded(!isExpanded)}
        className="flex items-center gap-2 text-sm text-blue-600 hover:text-blue-700 mb-4"
      >
        <ChevronDown size={16} className={`transition-transform ${isExpanded ? 'rotate-180' : ''}`} />
        {isExpanded ? 'Hide' : 'Show'} Examples
      </button>

      {isExpanded && (
        <div className="bg-blue-50 rounded p-4 mb-4 text-sm text-gray-700">
          {examples}
        </div>
      )}

      <textarea
        value={answer}
        onChange={(e) => setAnswer(e.target.value)}
        placeholder="Share your thoughts..."
        className="w-full px-4 py-3 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-600 mb-4"
        rows={4}
        disabled={isLoading}
      />

      <button
        onClick={handleSubmit}
        disabled={isLoading || !answer.trim()}
        className="w-full bg-blue-600 text-white py-2 rounded-lg hover:bg-blue-700 disabled:bg-gray-400 font-semibold"
      >
        {isLoading ? 'Processing...' : 'Next Question'}
      </button>
    </div>
  );
};
